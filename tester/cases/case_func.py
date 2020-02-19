from tester.config import TEST_LEVELS
from tester.utils.report import Reporter

cases_func = {}
for test_level in TEST_LEVELS:
    cases_func[test_level] = []


def func_level(level: str):
    def wrapper(func):

        global cases_func
        for test_level in TEST_LEVELS:
            if level == test_level:
                cases_func[test_level] += [func]

        return func
    return wrapper


@func_level('less')
def func_less():
    Reporter.header3('func less start')
    assert True
    Reporter.header3('func less complete')


@func_level('common')
def func_common():
    Reporter.header3('func common start')
    assert True
    Reporter.header3('func common complete')


@func_level('verbose')
def func_verbose():
    Reporter.header3('func verbose start')
    assert True
    Reporter.header3('func verbose complete')
