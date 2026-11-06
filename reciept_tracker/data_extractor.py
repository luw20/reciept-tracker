import datetime
import re

class DataExtractor:
    def __init__(self, data = ""):
         self.data = data


    def extractDate(text:str) -> datetime:
        if date := re.search(r"(([1-2][0-9])|([1-9])|(3[0-1]))/((1[0-2])|([1-9]))/[0-9]{4}", text):
           #Convert regex obj to string
           date_str = date.group()    
           #Convert the string you found to datetime object
           date_obj=datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        return date_obj

    def extractCreditCardNum(text:str) -> datetime:
            #TODO: change to credit card regex
            if date := re.search(r"(([1-2][0-9])|([1-9])|(3[0-1]))/((1[0-2])|([1-9]))/[0-9]{4}", text):
               #Convert regex obj to string
               date_str = date.group()    
               #Convert the string you found to datetime object
               date_obj=datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
               return date_obj