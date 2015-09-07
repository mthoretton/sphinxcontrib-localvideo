#!/usr/bin/env python
# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.parsers.rst import Directive

class localvideo(nodes.General,nodes.Element):
    pass


def visit(self, node):
    filename = node.filename
    content=u'''
        <video controls="">
            <source type="video/webm" src="/_static/videos/%s"></source>
            Your browser is not supporting not support HTML5 video
        </video>
    ''' % filename

    self.body.append(content)

def depart(self,node):
    pass


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
        node.filename = arg.split("/")[-1]
        return [node]


