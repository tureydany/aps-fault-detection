import sys,os

def get_error_message_detail(error,error_detail:sys):
    _,_,exc_tb=sys.exc_info() #The sys.exc_info function returns a 3-tuple with the exception, the exception's parameter, and a traceback object that pinpoints the line of Python that raised the exception.
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class SensorException(Exception):

    def __init__(self,error_message,error_detail:sys):
        self.error_message=get_error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message

