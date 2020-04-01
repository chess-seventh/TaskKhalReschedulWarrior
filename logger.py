"""
File: logger.py
Author: chess-seventh
Email: chess7th@pm.me
Github: https://github.com/chess-seventh
Description: Logger module
"""

import logging
from logging.config import fileConfig

fileConfig('logger.ini')
logger = logging.getLogger()
# stream_handler = logging.StreamHandler(stderr)
# stream_handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# stream_handler.setFormatter(formatter)
# logger.addHandler(stream_handler)
# logger.setLevel(DEBUG)
