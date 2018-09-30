# -*- coding: utf-8 -*-

import tornado


class HelloModule(tornado.web.UIModule):
    def render(self, *args, **kwargs):
        return '<h1>-Hello, UIModule- from UIModule</h1>'


class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string('modules/book.html', book=book)

    def embedded_css(self):
        return ".book {background-color:#F5F5F5}"

    def javascript_files(self):
        return "https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.14/jquery-ui.min.js"

    def embedded_javascript(self):
        return "document.write(\"<p>by adon</p>\")"

