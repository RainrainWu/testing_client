from tester.report import Reporter
from tester.config import TEST_LEVELS
from tester.cases.case_func import (
    case_func_less,
    case_func_common,
    case_func_verbose,
)
from tester.cases.case_regr import (
    case_regr_less,
    case_regr_common,
    case_regr_verbose
)
from tester.cases.case_perf import (
    case_perf_less,
    case_perf_common,
    case_perf_verbose
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


def run_test_list(test_list: list):
    for test in test_list:
        try:
            test()
        except TypeError:
            tpl = 'test object {NAME} not callable.'
            Reporter.error(tpl.format(NAME=test))


def run_func_test(level: str):
    Reporter.header1('func test')

    if check_level(level, TEST_LEVELS[0]):
        run_test_list(case_func_less)
    
    if check_level(level, TEST_LEVELS[1]):
        run_test_list(case_func_common)

    if check_level(level, TEST_LEVELS[2]):
        run_test_list(case_func_verbose)


def run_regr_test(level: str):
    Reporter.header1('regr test')

    if check_level(level, TEST_LEVELS[0]):
        run_test_list(case_regr_less)
    
    if check_level(level, TEST_LEVELS[1]):
        run_test_list(case_regr_common)

    if check_level(level, TEST_LEVELS[2]):
        run_test_list(case_regr_verbose)


def run_perf_test(level: str):
    Reporter.header1('perf test')

    if check_level(level, TEST_LEVELS[0]):
        run_test_list(case_perf_less)
    
    if check_level(level, TEST_LEVELS[1]):
        run_test_list(case_perf_common)

    if check_level(level, TEST_LEVELS[2]):
        run_test_list(case_perf_verbose)

