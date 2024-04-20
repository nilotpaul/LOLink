import logging
import yaml

with open('config/logger.config.yml', 'r') as file:
    logger_cfg = yaml.safe_load(file)

logger = logging.getLogger(logger_cfg['logger']['name'])
logger.setLevel(logger_cfg['logger']['level'])

log_format = logging.Formatter(logger_cfg['logger']['format'])

if 'file_handler' in logger_cfg['logger']['handlers']:
    file_config = logger_cfg['logger']['handlers']['file_handler']
    file_handler = logging.FileHandler(file_config['filename'])
    file_handler.setLevel(file_config['level'])
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

if 'console_handler' in logger_cfg['logger']['handlers']:
    console_config = logger_cfg['logger']['handlers']['console_handler']
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_config['level'])
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)
