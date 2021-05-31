"""Logging用Util"""

import logging

logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s[%(name)s][%(levelname)s] %(message)s'
)
logger = logging.getLogger('ROBOTER')
logger.setLevel(logging.DEBUG)


def debug(message):
    """DEBUGログ出力

    Args:
        message (str): ログ出力内容
    """
    logger.debug(message)


def info(message):
    """ログ出力

    Args:
        message (str): ログ出力内容
    """
    logger.info(message)
