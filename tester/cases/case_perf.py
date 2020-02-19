from tester.report import Reporter

case_perf_less = []
case_perf_common = []
case_perf_verbose = []


def perf_level(test_level: str):
    def wrapper(func):

        global case_perf_less, case_perf_common, case_perf_verbose
        if test_level == 'less':
            case_perf_less += [func]
        if test_level == 'common':
            case_perf_common += [func]
        if test_level == 'verbose':
            case_perf_verbose += [func]
    
        return func
    return wrapper


@perf_level('less')
def perf_less():
    Reporter.header3('perf less start')
    assert True
    Reporter.header3('perf less complete')


@perf_level('common')
def perf_common():
    Reporter.header3('perf common start')
    assert True
    Reporter.header3('perf common complete')


@perf_level('verbose')
def perf_verbose():
    Reporter.header3('perf verbose start')
    assert True
    Reporter.header3('perf verbose complete')
