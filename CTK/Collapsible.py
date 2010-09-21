# -*- coding: utf-8 -*-
#
# CTK: Cherokee Toolkit
#
# Authors:
#      Alvaro Lopez Ortega <alvaro@alobbs.com>
#
# Copyright (C) 2010 Alvaro Lopez Ortega
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 2 of the GNU General Public
# License as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

from Widget import Widget
from Box import Box


class Collapsible (Box):
    def __init__ (self, (titles), collapsed=True):
        Box.__init__ (self, {'class': 'collapsible'})

        self.collapsed = collapsed
        if collapsed:
            self.content = Box ({'class': 'collapsible-content', 'style': 'display:none;'})
        else:
            self.content = Box ({'class': 'collapsible-content'})

        assert len(titles) == 2
        self.title_show = Box ({'class': 'collapsible-title'}, titles[0])
        self.title_hide = Box ({'class': 'collapsible-title'}, titles[1])

        self.title_show.bind ('click', self.__JS_show())
        self.title_hide.bind ('click', self.__JS_hide())

        # Build up
        Box.__iadd__ (self, self.title_show)
        Box.__iadd__ (self, self.title_hide)
        Box.__iadd__ (self, self.content)

    def __iadd__ (self, content):
        self.content += content
        return self

    def __JS_show (self):
        return self.content.JS_to_show(100) + self.title_hide.JS_to_show() + self.title_show.JS_to_hide()

    def __JS_hide (self):
        return self.content.JS_to_hide() + self.title_hide.JS_to_hide() + self.title_show.JS_to_show()

    def Render (self):
        render = Box.Render (self)

        if self.collapsed:
            render.js += self.__JS_hide()
        else:
            render.js += self.__JS_show()

        return render
