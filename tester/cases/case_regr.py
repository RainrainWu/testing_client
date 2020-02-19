from tester.report import Reporter

case_regr_less = []
case_regr_common = []
case_regr_verbose = []


def regr_level(test_level: str):
    def wrapper(func):

        global case_regr_less, case_regr_common, case_regr_verbose
        if test_level == 'less':
            case_regr_less += [func]
        if test_level == 'common':
            case_regr_common += [func]
        if test_level == 'verbose':
            case_regr_verbose += [func]

        return func
    return wrapper


@regr_level('less')
def regr_less():
    Reporter.header3('regr less start')
    assert True
    Reporter.header3('regr less complete')


@regr_level('common')
def regr_common():
    Reporter.header3('regr common start')
    assert True
    Reporter.header3('regr common complete')


@regr_level('verbose')
def regr_verbose():
    Reporter.header3('regr verbose start')
    assert True
    Reporter.header3('regr verbose complete')
