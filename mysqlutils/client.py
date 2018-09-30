# -*- coding:utf-8 -*-

from littledb import pool, Connection
import config

configParser = config.configParser
dbConfig = dict(configParser.items('db'))
dbPool = None
# print("dbPool %s " % dbPool)


def conn():
    if dbPool is None:
        init()
    return Connection(host=dbConfig['host'] + ":" + dbConfig['port'],
                      database=dbConfig['database'],
                      user=dbConfig['user'],
                      password=dbConfig['pwd'],
                      pool=dbPool)


def init():
    dbPool = pool(host=dbConfig['host'],
                  port=int(dbConfig['port']),
                  database=dbConfig['database'],
                  user=dbConfig['user'],
                  password=dbConfig['pwd'])
    # print("dbPool %s " % dbPool)
