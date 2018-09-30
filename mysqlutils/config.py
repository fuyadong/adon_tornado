# -*- coding:utf-8 -*-

import ConfigParser
from settings import settings


config_rel_path = '/'.join((settings.get('app_path'), 'sysconfig.conf'))
configParser = ConfigParser.ConfigParser()
configParser.read(config_rel_path)

# db_section = configParser.items("db")
# print db_section
