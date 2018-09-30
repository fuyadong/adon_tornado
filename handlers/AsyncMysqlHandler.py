# -*- coding: utf-8 -*-

import time
import tornado.httpclient
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.gen


from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
from functools import partial, wraps

"""
py2: pip install futures
"""

EXECUTOR = ThreadPoolExecutor(max_workers=4)


def unblock(f):
    @tornado.web.asynchronous
    @wraps(f)
    def wrapper(*args, **kwargs):
        self = args[0]

        def callback(future):
            self.write(future.result())
            self.finish()

        EXECUTOR.submit(partial(f, *args, **kwargs)).add_done_callback(
            lambda future: tornado.ioloop.IOLoop.instance().add_callback(partial(callback, future)))
        return wrapper


class SleepHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(2)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        yield self.sleep()
        self.write("when i sleep")
        self.finish()

    @run_on_executor
    def sleep(self):
        time.sleep(5)
        # return 5


class NewSleepAsyncHandler(tornado.web.RequestHandler):
    """
    使用线程池，异步回调机制
    """
    @tornado.web.asynchronous
    def get(self, n):
        print time.time()

        def callback(future):
            print future.result()
            # self.write(future.result())
            # self.finish()

        EXECUTOR.submit(partial(self.get_, n)).add_done_callback(
            lambda future: tornado.ioloop.IOLoop.instance().add_callback(
                partial(callback, future)))

        self.write("before returned for time 2!")
        self.finish()

    def get_(self, n):
        time.sleep(float(n))
        return "Awake! %s" % time.time()


class NewSleepHandler(tornado.web.RequestHandler):
    """
    使用unblock装饰器实现并发任务
    目前此接口有问题
    """
    @unblock
    def get(self, n):
        time.sleep(float(n))
        return "Awake! %s" % time.time()


class JustNowHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("i hope just now see you")

