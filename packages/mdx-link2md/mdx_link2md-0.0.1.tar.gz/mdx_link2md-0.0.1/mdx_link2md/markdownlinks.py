"""
MarkdownLinks Extension for Python-Markdown
==========================================

Converts markdown links to another markdown file to a html file with the same name.
Helpful in converting documents in markdown format to HTML format in batch.

All changes Copyright 2018 -2014 The Python Markdown Project

License: [BSD](http://www.opensource.org/licenses/bsd-license.php)

TODO: Allow to run with -m flag from the command line
"""

from __future__ import absolute_import
from __future__ import unicode_literals
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re


class MarkdownLinkExtension(Extension):
    """ MarkdownLinks Extension for Python-Markdown. """

    def __init__(self, **kwargs):
        self.config = {
            'ignore_url': [True, 'Exclude URL links, which normally have "://" in them'],
        }

        super(MarkdownLinkExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        """ Insert MarkdownLinkPreprocessor before ReferencePreprocessor. """
        md.preprocessors.add('mdlink', MarkdownLinkPreprocessor(md, self), '<reference')


class MarkdownLinkPreprocessor(Preprocessor):
    """ MarkdownLinks Preprocessor - parse text for markdown links. """

    def __init__(self, md, ext):
        super(Preprocessor, self).__init__(md)

        if ext.getConfig('ignore_url'):
            self.link_pattern = r'((\[[^]]*\]\((((?!://)(?!.md\)).)*).)md)'
        else:
            self.link_pattern = r'((\[[^]]*\]\((((?!.md\)).)*).)md)'

        self.link_re = re.compile(self.link_pattern, flags=re.IGNORECASE)

    def run(self, lines):
        """
        Find and convert all MarkdownLinks from the text.
        """

        new_text = []
        for line in lines:
            m = self.link_re.search(line)
            if m:
                new_line = re.sub(self.link_pattern, r'\2html', line, flags=re.IGNORECASE)
                new_text.append(new_line)
            else:
                new_text.append(line)
        return new_text


def makeExtension(*args, **kwargs):
    return MarkdownLinkExtension(*args, **kwargs)
