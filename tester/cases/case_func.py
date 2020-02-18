from tester.report import Reporter


def func_less():
    assert True
    Reporter.header3('func less complete')


def func_common():
    assert True
    Reporter.header3('func common complete')


def func_verbose():
    assert True
    Reporter.header3('func verbose complete')
