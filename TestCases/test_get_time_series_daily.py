import requests
import pandas as pd
import pytest
from jsonschema import validate
from Utilities.log_generator import logGen
from Utilities.read_properties import readConfig
from datetime import date, timedelta

class Test_TIME_SERIES_DAILY:
    uri= readConfig.geturi()
    datafilepath = readConfig.getfilepath()
    symbolname = readConfig.getsymbol()
    logger = logGen.logger()

    @pytest.fixture(scope='package')
    def setup(self):
        url= self.uri+"/query?function=TIME_SERIES_DAILY&symbol="+self.symbolname+"&apikey=S6FWBQUYUHNRQK9V"
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

    def test_schemacheck(self,setup):
        #'''Validate the response schema and datatype'''
        self.logger.info("Test case test_schemacheck started")
        response= setup
        json_data = response.json()
        schema = {
            "type": "object",
            "properties": {
                "Meta Data": {
                    "type": "object",
                    "properties": {
                        "1. Information": {"type": "string"},
                        "2. Symbol": {"type": "string"},
                        "3. Last Refreshed": {"type": "string"}
                    },
                    "required": ["2. Symbol"]
                },
                "Time Series (Daily)": {
                    "type": "object",
                    "properties": {
                        "1. open": {"type": "number"},
                        "2. high": {"type": "number"},
                        "3. low": {"type": "number"},
                        "4. close": {"type": "number"},
                        "5. volume": {"type": "number"}
                    }
                }
            }
        }
        validate(instance=json_data, schema=schema)
        self.logger.info("Test case test_schemacheck finished")

    def test_datacountcheck(self,setup):
        #'''Validate the no of rows returned in response'''
        self.logger.info("Test case test_checkdatacount started")
        response= setup
        json_data = response.json()
        datacount = len(json_data['Time Series (Daily)'])
        assert datacount==100
        self.logger.info(datacount)
        self.logger.info("Test case test_checkdatcacount finished")

    def test_refreshdatecheck(self,setup):
        #'''Validate the last refresh date in response'''
        self.logger.info("Test case test_refreshdate started")
        response = setup
        json_data = response.json()
        time_dic = json_data['Time Series (Daily)']
        res_refreshdate = list(time_dic.keys())[0]
        today = date.today()
        systm_date = today - timedelta(days=1)
        assert str(res_refreshdate) == str(systm_date)
        #self.logger.info("response refresh date: ",res_refreshdate)
        self.logger.info("Test case test_refreshdate finished")

    def test_headercheck(self,setup):
        #'''Validate the header in response'''
        response = setup
        self.logger.info("Test case test_headercheck started")
        assert response.headers.get('X-Frame-Options')
        self.logger.info("Test case test_headercheck finished")


    def test_respsizecheck(self,setup):
        #'''Validate the response size'''
        response = setup
        self.logger.info("Test case test_respsizecheck started")
        resSize = len(response.content)
        assert resSize > 10000
        self.logger.info("Test case test_respsizecheck finished")

    def test_datacheck(self,setup):
        #'''Validate the data for dated 2020-12-16 '''
        response = setup
        self.logger.info("Test case test_datacheck started")
        json_data = response.json()
        time_dic = json_data['Time Series (Daily)']['2020-12-16']
        responselist = []
        for values in time_dic.values():
            responselist.append(values)
        responselist = [float(i) for i in responselist]

        # creating list from csv data for 2020-12-16
        df = pd.read_csv(self.datafilepath, skiprows=[1])
        csv_list = df.values
        print(len(csv_list))
        csvdata = []
        for i in range(len(csv_list)):
            csvdata.append(csv_list[i][1])
        listdiff = [x for x in responselist + csvdata if x not in responselist or x not in csvdata]
        self.logger.info(responselist)
        self.logger.info(csvdata)
        self.logger.info(listdiff)
        if not listdiff:
            assert True
        else:
            assert False
        self.logger.info("Test case test_datacheck finished")