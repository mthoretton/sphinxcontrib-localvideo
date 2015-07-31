# -*- coding: utf-8 -*-
"""
    sphinxcontrib
    ~~~~~~~~~~~~~

    This package is a namespace package that contains all extensions
    distributed in the ``sphinx-contrib`` distribution.

    :copyright: Copyright 2007-2009 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""


def setup(app):

    from . import localvideo

    app.add_node(localvideo.localvideo,
                 html=(localvideo.player))
    app.add_directive('localvideo', localvideo.localvideoDirective)
