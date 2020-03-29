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
