"""
logger.py
---------

Application logging utilities.
"""

from __future__ import annotations

import logging
from pathlib import Path

from config import ENABLE_LOGGING, LOG_FILE, LOG_LEVEL


_logger = None


def get_logger() -> logging.Logger:
    """
    Return the application's logger.

    The logger is created only once (Singleton pattern).
    """

    global _logger

    if _logger is not None:
        return _logger

    Path(LOG_FILE).parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    logger = logging.getLogger("PacketSniffer")

    logger.setLevel(LOG_LEVEL)

    if not logger.handlers:

        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        file_handler = logging.FileHandler(
            LOG_FILE,
            encoding="utf-8",
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    _logger = logger

    return logger


def log_debug(message: str) -> None:
    """
    Log a DEBUG message.
    """

    if ENABLE_LOGGING:
        get_logger().debug(message)


def log_info(message: str) -> None:
    """
    Log an INFO message.
    """

    if ENABLE_LOGGING:
        get_logger().info(message)


def log_warning(message: str) -> None:
    """
    Log a WARNING message.
    """

    if ENABLE_LOGGING:
        get_logger().warning(message)


def log_error(message: str) -> None:
    """
    Log an ERROR message.
    """

    if ENABLE_LOGGING:
        get_logger().error(message)


def log_exception(message: str) -> None:
    """
    Log an exception including the traceback.
    """

    if ENABLE_LOGGING:
        get_logger().exception(message)