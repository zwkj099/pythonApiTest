#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: leeyoshinari

import os
import logging.handlers
import config as cfg


class logger(object):
	LEVEL = cfg.LOG_LEVEL
	log_path = cfg.LOG_PATH

	if not os.path.exists(log_path):
		os.mkdir(log_path)

	log_level = {
		'DEBUG': logging.DEBUG,
		'INFO': logging.INFO,
		'WARNING': logging.WARNING,
		'ERROR': logging.ERROR,
		'CRITICAL': logging.CRITICAL
	}

	logger = logging.getLogger()
	formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s')
	logger.setLevel(level=log_level.get(LEVEL))

	# 日志输出到文件，仅保存最近10个日志文件
	file_handler = logging.handlers.TimedRotatingFileHandler(os.path.join(log_path, 'ATI.log'), when='midnight', interval=1, backupCount=10)
	file_handler.suffix = '%Y-%m-%d.log'

	# 日志输出到控制台
	# file_handler = logging.StreamHandler()

	file_handler.setFormatter(formatter)
	logger.addHandler(file_handler)
