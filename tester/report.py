from loguru import logger


class Reporter:

    __header1_length = 60
    __header1_split = '#'
    __header2_length = 50
    __header2_split = '='
    __header3_length = 40
    __header3_split = '-'

    @classmethod
    def header1(cls, title):
        logger.debug('')
        logger.debug('')
        mark = '[{TITLE}]'.format(TITLE=title)
        split_length = cls.__header1_length - len(mark)
        head = mark + cls.__header1_split * split_length
        logger.debug(head)
        logger.debug('')

    @classmethod
    def header2(cls, title):
        logger.debug('')
        mark = '[{TITLE}]'.format(TITLE=title)
        split_length = cls.__header2_length - len(mark)
        head = mark + cls.__header2_split * split_length
        logger.debug(head)
        logger.debug('')

    @classmethod
    def header3(cls, title):
        logger.debug('')
        mark = '[{TITLE}]'.format(TITLE=title)
        split_length = cls.__header3_length - len(mark)
        head = mark + cls.__header3_split * split_length
        logger.debug(head)

    @classmethod
    def error(cls, err):
        logger.error('  ' + err)