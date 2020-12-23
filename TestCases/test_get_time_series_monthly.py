import requests
import pandas as pd
import pytest
from jsonschema import validate
from Utilities.log_generator import logGen
from Utilities.read_properties import readConfig
from datetime import date, timedelta

class Test_TIME_SERIES_MONTHLY:
    uri= readConfig.geturi()
    datafilepath = readConfig.getfilepath()
    symbolname = readConfig.getsymbol()
    logger = logGen.logger()

    @pytest.fixture(scope='package')
    def setup(self):
        url= self.uri+"/query?function=TIME_SERIES_MONTHLY&symbol="+self.symbolname+"&apikey=S6FWBQUYUHNRQK9V"
        response= requests.get(url)
        return response

    def test_displayresponse(self,setup):
        #'''Display the response of the request in json format'''
        self.logger.info("Test case test_displayresponse started")
        response= setup
        json_data= response.json()
        self.logger.info(json_data)
        self.logger.info("Test case test_displayresponse finished")


    def test_statuscode(self,setup):
        #'''Validate the status code of the reponse'''
        response= setup
        self.logger.info("Test case test_statuscode started")
        assert response.status_code==200
        self.logger.info("Test case test_statuscode finished")

    def test_symbolcheck(self,setup):
        #'''Validate the symbol returned in the request is matched'''
        response = setup
        self.logger.info("Test case test_symbolcheck started")
        json_data= response.json()
        symbol= json_data['Meta Data']['2. Symbol']
        assert symbol==self.symbolname
        self.logger.info(symbol)
        self.logger.info(self.symbolname)
        self.logger.info("Test case test_symbolcheck finished")

    def test_invalidsymbol(self,setup):
        #'''Negative Test: Validate if we are passing invalid symbol'''
        response= setup
        self.logger.info("Test case test_invalidsymbol started")
        json_data = response.json()
        for key in json_data.keys():
            if key != 'Error Message':
                assert True
            else:
                assert False
        self.logger.info("Test case test_invalidsymbol finished")

    def test_badrequestcheck(self,setup):
        #'''Negative Test: Validate if we passing bad request'''
        response= setup
        self.logger.info("Test case test_badrequestcheck started")
        assert  response.status_code != 400
        self.logger.info("Test case test_badrequestcheck finished")