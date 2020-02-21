import os
import runpy
import pkgutil

from tester import case
from tester.case.case_manager import cases
from tester.utils.report import Reporter
from tester.config import (
    TEST_GROUPS,
    TEST_LEVELS
)

for importer, modname, ispkg in pkgutil.iter_modules(case.__path__):
    if modname != 'case_manager':
        runpy.run_module(mod_name='tester.case.' + modname)


def check_level(level, threshold):
    return TEST_LEVELS.index(level) >= TEST_LEVELS.index(threshold)


def run_test(group: str, level: str):

    for test_group in TEST_GROUPS:
        if group == test_group:
            Reporter.header1(group + ' test')
            
            for test_level in TEST_LEVELS:
                if check_level(level, test_level):
                    run_test_list(cases[test_group][test_level])


def run_test_list(test_list: list):

    for test in test_list:
        try:
            test()
        except TypeError:
            tpl = 'test object {NAME} not callable.'
            Reporter.error(tpl.format(NAME=test))
