from tester.config import TEST_LEVELS
from tester.utils.report import Reporter

cases_perf = {}
for test_level in TEST_LEVELS:
    cases_perf[test_level] = []


def perf_level(level: str):
    def wrapper(func):

        global cases_perf
        for test_level in TEST_LEVELS:
            if level == test_level:
                cases_perf[test_level] += [func]

        return func
    return wrapper


@perf_level('less')
def perf_less():
    Reporter.header3('perf less start')
    assert True
    Reporter.header3('perf less complete')


@perf_level('common')
def perf_common():
    Reporter.header3('perf common start')
    assert True
    Reporter.header3('perf common complete')


@perf_level('verbose')
def perf_verbose():
    Reporter.header3('perf verbose start')
    assert True
    Reporter.header3('perf verbose complete')
