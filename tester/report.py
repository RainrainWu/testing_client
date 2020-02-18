from loguru import logger


class Reporter:

    __header1 = '[{TITLE}]=================================================='
    __header2 = '[{TITLE}]----------------------------------------'
    __header3 = '[{TITLE}]--------------------'

    @classmethod
    def header1(cls, title):
        logger.debug('')
        logger.debug('')
        logger.debug(cls.__header1.format(TITLE=title))
        logger.debug('')

    @classmethod
    def header2(cls, title):
        logger.debug('')
        logger.debug(cls.__header2.format(TITLE=title))
        logger.debug('')

    @classmethod
    def header3(cls, title):
        logger.debug('')
        logger.debug(cls.__header3.format(TITLE=title))
