from tester.utils.report import Reporter
from tester.case.case_manager import mount


@mount('func', 'common')
def foo():
    Reporter.header3('test case foo start')
    assert True
    Reporter.header3('test case foo complete')


@mount('regr', 'less')
def bar():
    Reporter.header3('test case bar start')
    assert True
    Reporter.header3('test case bar complete')
