# -*- coding: utf-8 -*-

"""
# Copyright(c) 2017, WeSmart Artificial Intelligent Co.Ltd, All rights reserved.
# 
#
# Description: 
#     Desc
# Author: Fu adon
# Versions: 
#     Created by Fu adon on 2018/9/20 下午12:05 for version 1.0
#     Modified by Fu adon on 2018/9/20 下午12:05 form version 1.0
"""

# import os
import logging
from logging.handlers import RotatingFileHandler

# if 'DEPLOYMENT_TYPE' in os.environ:
#     DEPLOYMENT = os.environ['DEPLOYMENT_TYPE'].upper()
# else:
#     DEPLOYMENT = "DEV"
#
# if DEPLOYMENT == "PROD":
#     LOG_PATH = '/mnt'
# else:
#     LOG_PATH = os.path.abspath(os.path.split(os.path.realpath(__file__))[0]+'/../')

LOG_PATH = '/tmp'
LOG_FILENAME = '/'.join([LOG_PATH, 'logs', 'consumer.log'])
logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(LOG_FILENAME, mode='a', maxBytes=1024*1024*1024, backupCount=5)
formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

