# app/utils/logging.py

## Example usage - Use this utility in routes or services:
# from app.utils.logging import setup_logger
#
# logger = setup_logger(__name__)
# logger.info("This is a log message.")
##

import logging

# def setup_logger(name: str) -> logging.Logger:
#     """
#     Setup and return a logger with consistent formatting.
#     """
#     logger = logging.getLogger(name)
#     if not logger.handlers:
#         handler = logging.StreamHandler()
#         formatter = logging.Formatter(
#             "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
#         )
#         handler.setFormatter(formatter)
#         logger.addHandler(handler)
#         logger.setLevel(logging.INFO)
#     return logger

logging.basicConfig(
    format="%(asctime)s [%(levelname)s]: %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)