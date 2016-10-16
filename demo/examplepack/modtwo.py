import logging
import os
from datetime import datetime

import requests


def log_something():
    """Bad logging practice"""
    logging.info("wrote to the log")


def return_something():
    return "Something"
