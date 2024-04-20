import os
from dotenv import load_dotenv
from logs.logger import logger

load_dotenv('./.env')

def get_env(key: str, fallback: any = ''):
    env_var: str = os.getenv(key)

    if len(env_var) == 0:
        logger.error(f'{key} variable not set')
    
        return fallback
    
    return env_var
    
