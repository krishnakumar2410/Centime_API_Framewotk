** Centime API Framework

# Tools/Technology Used
- Python, Pycharm, Pandas
- Framework: Pytest

1. Install Pycharm editor if not already installed
2. Go to file and click on create new project> Import downloaded project from GIT

#  Packages Required
- requests
- pytest
- json
- jsonpath
- pandas
- jsonschema
- datetime

For installation, go to Pycharm: File>Setting>Project:>Python Interpreter > Add package
From command line: pip install package_name or python -m pip install package_name

#  Framework Folder Structure
- Project Name: Centime_API_Framework
- Logs: Execution logs getting stored here
- Reports : Html file gets generated here, which we can open and check execution results for __pass/fail__ in browser
- TestCases: All the api test cases are created here
- Utilities : Here logger file created to print and store the logs for each execution. Additionaly ReadProperties is there which reads the url and path of the test data file from config.ini
- Configuration: Here I have created config file where I have mentioned the common uri and data file path
- Test Data: Here I have kept the expected values for dated 2020-12-16 in csv file which I am using under which I am comparing with response values


# Test Cases Covered [Most of test cases I have covered in time_seriesd_daily request. In other 4 I have just included 4-5 test cases each, we can replicate the same from time_seriesd_daily for more test cases]
1. Status code check
2. Schema/DataType check using jsonschema validate method
3. Number of items returned in response
4. Header Check 
5. Validation for bad parameter pass to requests
6. Reposne size
7. Data check csv vs response
8. Display response
9. Symbol returned in response vs symbol we passed
10. Invalid symbol check 
11. Refresh date check which is current day - 1 [Here I have checked againts IST time]

#  Steps to execute the test cases
- Go to terminal tab of the Pycharm
- Use below command to run

pytest -v TestCases --html=Reports/SuiteExecutionResult.html # This is for all the test cases to run at on go
pytest -v TestCases/test_get_time_series_daily.py --html=Reports/test_get_time_series_daily.html

Change test case name for others and html report name

# Reports 
- After execution go to the Reports folder and open the html file in browser for pass and failure results
