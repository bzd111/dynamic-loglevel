#coding:utf-8

import logging
log = logging.getLogger("Mymoudle")

def crawler(url="www.baidu.com"):
    log.info("Doin' stuff...")
    log.debug("debug crawler {}".format(url))
    pass
