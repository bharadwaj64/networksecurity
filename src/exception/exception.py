import sys 
from src.logging.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename 
    error_message = "error occured in python script {0}, line number {1}, error message {2}".format(filename,exc_tb.tb_lineno,str(error))
    return error_message 

class CustomException(Exception):
    def __init__(self,error,error_detail:sys):
        logging.info('exception has been created')
        super().__init__(error) 
        self.error = error 
        self.error_detail = error_detail
        self.error_message = error_message_detail(self.error,self.error_detail)
    
    def __str__(self):
        return self.error_message


