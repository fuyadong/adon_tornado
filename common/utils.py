# -*- coding: utf-8 -*-

"""
# Copyright(c) 2017, WeSmart Artificial Intelligent Co.Ltd, All rights reserved.
# 
#
# Description: 
#     公共方法
# Author: Fu adon
# Versions: 
#     Created by Fu adon on 2018/9/15 下午4:17 for version 1.0
#     Modified by Fu adon on 2018/9/15 下午4:17 form version 1.0
"""

import hashlib
from settings import settings


def mod_cal(src_str):
    """
    对给定的字符串，计算md5值，然后对md5值进行hash，最后根据CPU core值取模
    :param src_str:
    :return:
    """
    if not src_str:
        return None
    if not isinstance(src_str, str):
        src_str = str(src_str)
    md5_val = hashlib.md5(src_str.encode('utf-8')).hexdigest()
    hash_val = hash(md5_val)

    cpu_cores = settings.get('cpuCores', None)
    if not cpu_cores or cpu_cores < 1:
        return None

    if isinstance(hash_val, int):
        return hash_val % cpu_cores
    else:
        return None
