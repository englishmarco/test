from loguru import logger
import os


debug_logs_path = os.path.dirname(__file__) + '\\debug.log'
info_logs_path = os.path.dirname(__file__) + '\\info.log'
error_logs_path = os.path.dirname(__file__) + '\\error.log'

# logger.remove(handler_id=None)
# 禁止控制台输出日志

"""
日志配置信息
:param debug_logs_path  debug日志存放目录
:param info_logs_path   info日志存放目录
:param error_logs_path  error日志存放目录

"""

logger.add(debug_logs_path,
           filter=lambda x: x['level'].name == 'DEBUG',
           enqueue=True,
           rotation='00:00',
           encoding='utf-8',
           retention='30 days'
           )

logger.add(info_logs_path,
           filter=lambda x: x['level'].name > 'ERROR',
           # level='INFO',
           enqueue=True,
           rotation='00:00',
           encoding='utf-8',
           retention='30 days'
           )
logger.add(error_logs_path,
           filter='',
           level='WARNING',
           enqueue=True,
           rotation='00:00',
           encoding='utf-8',
           retention='30 days'
           )
