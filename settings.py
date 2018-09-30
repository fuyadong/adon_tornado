# -*- coding: utf-8 -*-

import os
import ConfigParser
from multiprocessing import cpu_count

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    app_path=os.path.dirname(__file__),
    debug=True,
    cpuCores=cpu_count(),
)

config_rel_path = '/'.join((settings.get('app_path'), 'sysconfig.conf'))
configParser = ConfigParser.ConfigParser()
configParser.read(config_rel_path)
# db_section = configParser.items("db")
# print db_section
