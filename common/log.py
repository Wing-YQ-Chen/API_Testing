import os
import time
import logging
import sys
from threading import current_thread
from loguru import logger


def setup_logging(log_dir_path: str = './Logs', level: int = logging.INFO):
    if not os.path.exists(log_dir_path):
        os.makedirs(log_dir_path)
    loger: logging.Logger = logging.getLogger()
    loger.setLevel(level)
    formatter = logging.Formatter('%(asctime)s %(threadName)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')
    ts = time.strftime('%Y%m%d%H%M%S', time.localtime()).__str__()
    fh = logging.FileHandler(
        os.path.join(log_dir_path, "{} {} {}.log".format(ts, current_thread().name, os.getlogin())), encoding="utf-8")
    fh.setFormatter(formatter)

    stream_handle = logging.StreamHandler()
    stream_handle.setFormatter(formatter)

    loger.addHandler(fh)
    loger.addHandler(stream_handle)

    return loger


def setup_loguru(log_dir_path, level="DEBUG"):
    # log level: TRACE < DEBUG < INFO < SUCCESS < WARNING < ERROR
    username = os.getlogin()
    log_path = os.path.join(log_dir_path, username + " {time}.log")

    logger.add(log_path,
               # format=r'{time:YYYY-MM-DD HH:mm:ss} | {file} | {process.name} | {thread.name} | {level} | {message}',
               format=r'{time:YYYY-MM-DD HH:mm:ss} | {file}-{thread.name} | {level} | {message}',
               level=level,
               encoding="utf-8",
               enqueue=True,
               colorize=True)
    # logger.configure(handlers=[{"sink": sys.stderr, "serialize": False}])