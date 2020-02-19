from tester.report import Reporter

case_func_less = []
case_func_common = []
case_func_verbose = []


def func_level(test_level: str):
    def wrapper(func):

        global case_func_less, case_func_common, case_func_verbose
        if test_level == 'less':
            case_func_less += [func]
        if test_level == 'common':
            case_func_common += [func]
        if test_level == 'verbose':
            case_func_verbose += [func]
    
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
