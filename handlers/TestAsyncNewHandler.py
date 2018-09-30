# -*- coding: utf-8 -*-

"""
异步操作Mysql数据库接口
"""

import time
import tornado
from mysqlutils import client
from concurrent.futures import ThreadPoolExecutor


class AsyncSQLHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(2)
    io_loop = tornado.ioloop.IOLoop.current()

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self, *args, **kwargs):
        # print self.get_query_argument("test")
        time = yield tornado.gen.Task(self.runSql)
        print time
        self.write(unicode(time))
        print "over"
        self.finish()

    @tornado.concurrent.run_on_executor
    def runSql(self):
        t = time.time()
        db = client.conn()
        record = db.get("SELECT * FROM customer_info where device_id='00D051AC0003';")
        print "record=%s" % record
        print record.get('buz_url')
        # db.execute("SELECT * FROM customer_info where device_id='00D051AC0003';")
        db.close()
        return time.time() - t


class SyncSQLHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        t = self.runSql()
        print time
        self.write(unicode(t))
        print "over"

    def runSql(self):
        t = time.time()
        db = client.conn()
        record = db.get("SELECT * FROM customer_info where device_id='00D051AC0003';")
        # db.execute("SELECT * FROM customer_info where device_id='00D051AC0003';")
        print "record=%s" % record
        print record.get('buz_url')
        db.close()
        return time.time() - t