from jennifer.api.task import force_shutdown
import logging
from jennifer.agent import jennifer_agent
from jennifer.hooks import hooking
from jennifer.api.config import ConfigNotExistsError


def setup_log(config):
    logger = logging.getLogger('jennifer')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.FileHandler(config.log_path)
    formatter = logging.Formatter(
        '%(asctime)s [JENNIFER] %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.info("Agent Start!")


def init(config):
    agent = jennifer_agent()
    agent.set_config(config)
    hooking()
