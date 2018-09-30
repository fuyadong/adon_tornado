# -*- coding: utf-8 -*-

import json
import random
import tornado
from common._redis import redisClient
from common.utils import mod_cal
from common.constants import BASE_MCU_QUEUE, BASE_ROUTER_QUEUE
from settings import settings


class PushMCUTaskHandler(tornado.web.RequestHandler):
    def get(self):
        # key = "url_00D051AC0007"
        # value = redisClient.hgetall(key)
        # print value
        # print type(value)

        cpu_cores = settings.get('cpuCores')
        dids = ['00D051AD042D', '00D051AD0008', '00D051AD0521', '00D051AD0565']
        rdm = random.randint(0, 100)
        # value = dids[rdm % cpu_cores]
        value = dids[rdm % 4]

        mod = mod_cal(value)
        q_key = ''.join((BASE_MCU_QUEUE, str(mod+1)))
        print("push [%s] to %s" % (value, q_key))
        try:
            redisClient.rpush(q_key, value)
            # redisClient.rpush(MCU_QUEUE, dids[rdm % 4])
        except Exception as e:
            print "Err: %s" % e
        self.write("Done!")


class PopMCUTaskHandler(tornado.web.RequestHandler):
    def get(self, mod):
        print "mod=%s" % mod
        # value = redisClient.rpop("DelayQueue")
        q_key = ''.join(('DelayQueue', str(mod)))
        try:
            value = redisClient.blpop(q_key)
        except Exception as e:
            print "Err: %s" % e
        print value
        self.write(json.dumps(value))


class PushRouterTaskHandler(tornado.web.RequestHandler):
    def get(self):
        # key = "url_00D051AC0007"
        # value = redisClient.hgetall(key)
        # print value
        # print type(value)

        dids = ['router_00D051AD042D', 'router_00D051AD0008', 'router_00D051AD0521', 'router_00D051AD0565']
        rdm = random.randint(0, 100)
        # value = dids[rdm % cpu_cores]
        value = dids[rdm % 4]
        mod = mod_cal(value)
        q_key = ''.join((BASE_ROUTER_QUEUE, str(mod+1)))
        print("push [%s] to %s" % (value, q_key))
        try:
            redisClient.rpush(q_key, value)
            # redisClient.rpush(BASE_ROUTER_QUEUE, dids[rdm % 4])
        except Exception as e:
            print "Err: %s" % e
        self.write("Done!")
