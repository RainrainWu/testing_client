from tester.utils.report import Reporter
from tester.config import (
    TEST_GROUPS,
    TEST_LEVELS
)


cases = {}
for test_group in TEST_GROUPS:
    cases[test_group] = {}
    for test_level in TEST_LEVELS:
        cases[test_group][test_level] = []


def mount(group: str, level: str):
    def wrapper(func):

        global cases
        for test_level in TEST_LEVELS:
            if level == test_level:
                cases[group][level] += [func]

        return func
    return wrapper
