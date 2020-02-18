from tester.report import Reporter
from tester.config import TEST_LEVELS
from tester.cases.case_func import (
    func_less,
    func_common,
    func_verbose
)


def check_level(level, threshold):
    return TEST_LEVELS.index(level) >= TEST_LEVELS.index(threshold)


def run_test(test_type: str, test_level: str):

    if test_type == 'func':
        run_func_test(test_level)
    elif test_type == 'regr':
        run_regr_test(test_level)
    elif test_type == 'perf':
        run_perf_test(test_level)
    else:
        return False


def run_func_test(level):
    Reporter.header1('func test')

    if check_level(level, TEST_LEVELS[0]):
        func_less()
    
    if check_level(level, TEST_LEVELS[1]):
        func_common()

    if check_level(level, TEST_LEVELS[2]):
        func_verbose()


def run_regr_test():
    Reporter.header1('regr test')


def run_perf_test():
    Reporter.header1('perf test')
