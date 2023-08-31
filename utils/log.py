import os
import logging
from datetime import datetime
from PublicSearch.settings import BASE_DIR


class Logger:
    def __init__(self, log_dir=os.path.join(BASE_DIR, 'logs')):
        self.log_dir = log_dir
        self.log_levels = ['info', 'error', 'debug', 'warning', 'critical']
        self.loggers = self.setup_custom_loggers()

    def setup_custom_loggers(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        loggers = {}

        for level in self.log_levels:
            logger = logging.getLogger(level)
            logger.setLevel(logging.getLevelName(level.upper()))

            date_str = datetime.now().strftime('%Y-%m-%d')
            log_file = os.path.join(self.log_dir, f'{level}{date_str}.log')

            formatter = logging.Formatter('%(asctime)s -%(levelname)s- File:%(filename)s[Line:%(lineno)d]：%(message)s')
            handler = logging.FileHandler(log_file)
            handler.setFormatter(formatter)

            logger.addHandler(handler)
            loggers[level] = logger

        return loggers

    def __getattr__(self, level):
        if level in self.log_levels:
            return self.loggers[level].info if level == 'info' else self.loggers[level].error
        raise AttributeError(f"CustomLogger object has no attribute '{level}'")


# Usage
if __name__ == '__main__':
    logger = Logger()
    try:
        logger.info('This is an info message')
        a
    except Exception as e:
        logger.error(f'This is an error message{e}', exc_info=True)
        logger.debug(f'This is an error message{e}', exc_info=True)
        logger.critical(f'This is an error message{e}', exc_info=True)
        logger.warning(f'This is an error message{e}', exc_info=True)