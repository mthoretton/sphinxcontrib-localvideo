#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.statemachine import ViewList
from sphinx.util.nodes import nested_parse_with_titles


class localvideo(nodes.Element):
    pass


class localvideoDirective(Directive):
    has_content = True
    option_spec = {
            }

    def run(self):
        #env = self.state.document.settings.env
        nodeRoot = nodes.section()
        nodeRoot.document = self.state.document

        result = ViewList()

        result.append('<video>')
        result.append('</video>')

        nested_parse_with_titles(self.state, result, nodeRoot)
        return nodeRoot.children


def setup(app):
    app.add_node(localvideo)
    app.add_directive('localvideo', localvideoDirective)
