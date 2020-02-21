from tester.utils.report import Reporter
from tester.config import (
    TEST_GROUPS,
    TEST_LEVELS
)


# Init case storage area
cases = {}
for test_group in TEST_GROUPS:
    cases[test_group] = {}
    for test_level in TEST_LEVELS:
        cases[test_group][test_level] = []


def mount(group: str, level: str):
    """Mount test case into test case storage area"""
    def wrapper(func):

        global cases
        for test_level in TEST_LEVELS:
            if level == test_level:
                cases[group][level] += [func]

        return func
    return wrapper
