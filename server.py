# -*- coding: utf-8 -*-

################################################################################
#
# Copyright(c) 2017, WeSmart Artificial Intelligent Co.Ltd, All rights reserved.
# 
#
# Description: 
# Desc
# Author: Fu adon
# Versions: 
#     Created by Fu adon on 2018/1/6 下午6:15 for version 1.0
#     Modified by Fu adon on 2018/1/6 下午6:15 form version 1.0
#
################################################################################


import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import pymongo
from settings import settings
from urls import handlers
from module import HelloModule, BookModule
from tornado.options import options, define

define("port", default=8000, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        # mongo_client = pymongo.MongoClient('localhost', 27017)
        # self.db = mongo_client.test_db
        settings['ui_modules'] = {'Hello': HelloModule, 'Book': BookModule}
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
    # tornado.ioloop.IOLoop.current().spawn_callback()
