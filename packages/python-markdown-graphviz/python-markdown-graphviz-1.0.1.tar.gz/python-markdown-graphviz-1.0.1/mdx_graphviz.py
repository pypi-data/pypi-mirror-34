# -*- coding: utf-8 -*-
# based on https://github.com/sprin/markdown-inline-graphviz

"""
Graphviz extensions for Markdown.
Renders the output inline, eliminating the need to configure an output
directory.

Supports outputs types of SVG and PNG. The output will be taken from the
filename specified in the tag. Example:

{% dot attack_plan.svg
    digraph G {
        rankdir=LR
        Earth [peripheries=2]
        Mars
        Earth -> Mars
    }
%}

Requires the graphviz library (http://www.graphviz.org/)

Inspired by jawher/markdown-dot (https://github.com/jawher/markdown-dot)
"""

import re
import markdown
import base64
import graphviz

# Global vars
BLOCK_RE = re.compile(
    r'^\{% (?P<command>\w+)\s+(?P<filename>[^\s]+)\s*\n(?P<content>.*?)%}\s*$',
    re.MULTILINE | re.DOTALL)
# Command whitelist
SUPPORTED_COMMAMDS = ['dot', 'neato', 'fdp', 'sfdp', 'twopi', 'circo']


class InlineGraphvizExtension(markdown.Extension):

    def extendMarkdown(self, md, md_globals):
        """ Add InlineGraphvizPreprocessor to the Markdown instance. """
        md.registerExtension(self)

        md.preprocessors.add('graphviz_block',
                             InlineGraphvizPreprocessor(md),
                             "_begin")


class InlineGraphvizPreprocessor(markdown.preprocessors.Preprocessor):

    def __init__(self, md):
        super(InlineGraphvizPreprocessor, self).__init__(md)

    def run(self, lines):
        """ Match and generate dot code blocks."""

        text = "\n".join(lines)
        while True:
            m = BLOCK_RE.search(text)
            if not m:
                break
            command = m.group('command')
            # Whitelist command, prevent command injection.
            if command not in SUPPORTED_COMMAMDS:
                raise Exception('Command not supported: %s' % command)
            filename = m.group('filename')
            content = m.group('content')
            filetype = filename[filename.rfind('.') + 1:]

            try:
                src = graphviz.Source(content)
                output = src.pipe(format=filetype)

                if filetype == 'svg':
                    data_url_filetype = 'svg+xml'
                    img = output.decode('utf-8')

                if filetype == 'png':
                    data_url_filetype = 'png'
                    encoding = 'base64'
                    output = base64.b64encode(output).decode()
                    data_path = "data:image/%s;%s,%s" % (
                        data_url_filetype,
                        encoding,
                        output)
                    img = "![" + filename + "](" + data_path + ")"

                text = '%s\n%s\n%s' % (
                    text[:m.start()], img, text[m.end():])
            except Exception as err:
                text = '%s\n%s\n%s' % (
                    text[:m.start()], str(err), text[m.end():])
        return text.split("\n")


def makeExtension(*args, **kwargs):
    return InlineGraphvizExtension(*args, **kwargs)
