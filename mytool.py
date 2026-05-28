# -*- coding: UTF-8 -*-
import inspect
import logging
import time
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter, StreamHandler as ColorStreamHandler
import os


class MyLogger(logging.Logger):
    def __init__(self, name, level=logging.DEBUG, log_file=None, max_log_size=1024 * 1024 * 9, backup_count=10):
        """
        :param name: test_logger
        :param level: 日记显示等级
        :param log_file: 传入输出地址，自动输出日记
        :param max_log_size: 日记最大大小，默认9M
        :param backup_count: 日记保存的数量
        """
        super().__init__(name, level)

        # formatter = logging.Formatter('[%(asctime)s] - %(levelname)s  - %(funcName)s : %(message)s')
        formatter = ColoredFormatter(
            '[%(asctime)s] - %(log_color)s%(levelname)s%(reset)s - %(log_color)s%(funcName)s : %(log_color)s%(message)s',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            }
        )

        # 控制台输出
        console_handler = ColorStreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        self.addHandler(console_handler)

        # 文件输出
        if log_file:
            # 如果指定了日志文件路径，确保目录存在，如果不存在则创建
            log_dir = os.path.dirname(log_file)
            print(log_dir)
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            # 创建RotatingFileHandler，设定最大日志文件大小和备份文件数
            file_handler = RotatingFileHandler(log_file, mode='a', maxBytes=max_log_size, backupCount=backup_count,
                                               encoding='utf-8')
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            self.addHandler(file_handler)

log_directory = f"./log/{time.strftime('%Y%m%d')}.log"
logger = MyLogger('test_logger', log_file=log_directory, max_log_size=1024 * 1024 * 100, backup_count=20)
