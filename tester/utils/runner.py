from tester.config import TEST_LEVELS
from tester.utils.report import Reporter
from tester.cases.case_func import cases_func
from tester.cases.case_regr import cases_regr
from tester.cases.case_perf import cases_perf


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
    for test_level in TEST_LEVELS:
        if check_level(level, test_level):
            run_test_list(cases_func[test_level])


def run_regr_test(level: str):

    Reporter.header1('regr test')
    for test_level in TEST_LEVELS:
        if check_level(level, test_level):
            run_test_list(cases_regr[test_level])


def run_perf_test(level: str):

    Reporter.header1('perf test')
    for test_level in TEST_LEVELS:
        if check_level(level, test_level):
            run_test_list(cases_perf[test_level])
