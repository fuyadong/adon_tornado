# -*- coding: utf-8 -*-

"""
# Copyright(c) 2017, WeSmart Artificial Intelligent Co.Ltd, All rights reserved.
# 
#
# Description: 
#     Router Info 更新状态消息消费者进程
# Author: Fu adon
# Versions: 
#     Created by Fu adon on 2018/9/15 下午5:50 for version 1.0
#     Modified by Fu adon on 2018/9/15 下午5:50 form version 1.0
"""

# import os
# import platform
from logger import logger
from common._redis import redisClient
from multiprocessing import Pool, cpu_count
from common.constants import BASE_ROUTER_QUEUE


def do_task(queue_name, params):
    """
    :return:
    """
    # print "do task: %s from queue: %s" % (queue_name, params)
    logger.info("do task: %s from queue: %s", queue_name, params)

# os_name = platform.system()
# if os_name.lower() == 'linux':
#     cores_cmd = "cat /proc/cpuinfo | grep 'processor'|sort -u|wc -l"
#     os.system(cores_cmd)


if __name__ == '__main__':
    # 1. 初始化进程池
    cpu_cores = cpu_count()
    pool = Pool(processes=cpu_cores)

    q_keys = [''.join([BASE_ROUTER_QUEUE, str(core)]) for core in range(1, cpu_cores + 1)]
    logger.info("q_keys: %s", q_keys)
    # 2. 主进程启动时清除queue
    redisClient.delete(BASE_ROUTER_QUEUE)
    while True:
        # 3.  从队列中取task，两个队列：mcuQueue and routerQueue
        try:
            queue_key, task = redisClient.blpop(q_keys)
        except Exception as e:
            # print "Err: %s" % e
            logger.info("Err: %s", e)
        # print "value: %s from %s" % (task, queue_key)
        logger.info("value: %s from %s", task, queue_key)

        # 4. 若队列任务task不为空，扔到进程池
        if task:
            pool.apply_async(do_task, (queue_key, task))

        # 5. 进程执行成功后，主进程再从队列中取任务
        # TODO: goto while True
