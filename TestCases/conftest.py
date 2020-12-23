import pytest
from py.xml import html

def pytest_configure(config):
    config._metadata['Project Name']= 'Centime_API_Project'
    config._metadata['Module Name']= 'alphavantage'
    config._metadata['QA Name'] = 'Krishna Mokadam'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins",None)

def pytest_html_report_title(report):
    report.title= 'Alphavantage API Report'

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring