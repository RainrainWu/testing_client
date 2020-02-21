from tester.utils.report import Reporter
from tester.case.case_manager import mount


@mount('func', 'less')
def func_less():
    Reporter.header3('func less start')
    assert True
    Reporter.header3('func less complete')


@mount('func', 'common')
def func_common():
    Reporter.header3('func common start')
    assert True
    Reporter.header3('func common complete')
