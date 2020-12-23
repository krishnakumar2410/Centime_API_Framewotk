import configparser

config= configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class readConfig:

    @staticmethod
    def geturi(): # Lets say this is for QA env
        uri= config.get('common info','uri')
        return uri

    @staticmethod
    def getfilepath():
        path_data_file = config.get('common info', 'datafilepath')
        return path_data_file

    @staticmethod
    def getsymbol():
        symbolname = config.get('common info', 'symbol')
        return symbolname
