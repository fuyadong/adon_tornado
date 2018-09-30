# -*- coding: utf-8 -*-

from redis import client
from settings import configParser

redis_section = dict(configParser.items("redis"))
password = redis_section.get("redis.password") if str(redis_section.get("redis.password")) != 'None' else ""
redisClient = client.StrictRedis(host=redis_section.get("redis.host"),
                                 port=redis_section.get("redis.port"),
                                 db=redis_section.get("redis.db"),
                                 password=password)
