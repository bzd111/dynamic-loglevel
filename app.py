# coding: utf-8
import logging
import traceback

from flask import Flask, request

import settings
from mymoudle import crawler
app = Flask(__name__)
logger = logging.getLogger('app')


@app.route('/')
def hello_world():
    logger.debug("DEBUG: Hello, world")
    logger.info("INFO: Hello, World")
    crawler()
    return 'Hello World!'


@app.route('/loglevel', methods=['GET', 'POST'])
def loglevel():
    if request.method == 'POST':
        error = ''
        content = request.json
        LOG_LEVEL = content["LOG_LEVEL"]
        logger.warn('Setting logger level to ANT_LOG_LEVEL: {}'.format(
            LOG_LEVEL))
        for name in settings.LOGGING['loggers']:
            try:
                logger_ = logging.getLogger(name)
                logger_.setLevel(LOG_LEVEL)
                for handler in logger_.handlers:
                    handler.setLevel(LOG_LEVEL)
            except Exception:
                logger.error(traceback.format_exc())
                error += traceback.format_exc() + '\n'
        if error:
            return 'Set logger level to LOG_LEVEL: {} failed.\n{}'.format(LOG_LEVEL, error)
        else:
            return 'Set logger level to LOG_LEVEL: {} success'.format(LOG_LEVEL)
    else:
        return "Hello"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=settings.FRAMEWORK_PORT, debug=True)
