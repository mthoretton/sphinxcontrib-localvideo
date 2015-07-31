#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import Directive

class localvideo(nodes.General,nodes.Element):
    pass


def player(self, node):
    filepath = node.filepath
    content=u'''
        <video>
        <src='%s'/>
        </video>
    ''' % filepath

    content = "BONJOUR"
    self.body.append(content)


class localvideoDirective(Directive):
    name = 'localvideo'
    node_class = localvideo

    has_content = False
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = False
    option_spec = {}

    def run(self):
        node = self.node_class()
        arg = self.arguments[0]
        node.filepath = arg
        return [node]


