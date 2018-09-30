# -*- coding: utf-8 -*-

from handlers.LearnHandler import *
from handlers.AsyncMysqlHandler import SleepHandler, JustNowHandler, NewSleepAsyncHandler, NewSleepHandler
from handlers.TestAsyncNewHandler import AsyncSQLHandler, SyncSQLHandler
from handlers.RedisQueueHandler import PushMCUTaskHandler, PopMCUTaskHandler, PushRouterTaskHandler

handlers = [
    (r'/', MainHandler),
    (r'^/reverse/(\w+)$', ReverseHandler),
    (r'/wrap', WrapHandler),
    (r'/widget/(\d+)', WidgetHandler),
    (r'/index', IndexHandler),
    (r'/poem', PoemPageHandler),
    (r'/books', GetBooksHandler),
    (r'/books/edit/([0-9Xx\-]+)', BookEditHandler),
    (r"/books/add", BookEditHandler),
    (r'/alpha_mge', AlphaMge),
    (r'/word/(\w+)', WordHandler),
    # Test1
    (r"/justnow", JustNowHandler),
    (r"/sleep", SleepHandler),
    (r"/newsleep/(\d+)", NewSleepHandler),
    (r"/sleep_async/(\d+)", NewSleepAsyncHandler),
    # Test2
    ("/async", AsyncSQLHandler),
    ("/sync", SyncSQLHandler),
    # redis push/pop
    ("/pushMcuRedis", PushMCUTaskHandler),
    ("/popMcuRedis/(\d+)", PopMCUTaskHandler),
    ("/pushRouterRedis", PushRouterTaskHandler),
]

