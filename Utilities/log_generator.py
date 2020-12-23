import logging

class logGen:
    @staticmethod
    def logger():

        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=".\\Logs\\ApiExecution.log", filemode='a',format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger= logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


