from tester.config import TEST_LEVELS
from tester.utils.report import Reporter

cases_regr = {}
for test_level in TEST_LEVELS:
    cases_regr[test_level] = []


def regr_level(level: str):
    def wrapper(func):

        global cases_regr
        for test_level in TEST_LEVELS:
            if level == test_level:
                cases_regr[test_level] += [func]

        return func
    return wrapper


@regr_level('less')
def regr_less():
    Reporter.header3('regr less start')
    assert True
    Reporter.header3('regr less complete')


@regr_level('common')
def regr_common():
    Reporter.header3('regr common start')
    assert True
    Reporter.header3('regr common complete')


@regr_level('verbose')
def regr_verbose():
    Reporter.header3('regr verbose start')
    assert True
    Reporter.header3('regr verbose complete')
