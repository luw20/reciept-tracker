import datetime
import re

class DataExtractor:
    def __init__(self, data = ""):
         self.data = data


    def extractDate(self, text:str) -> datetime:
        date_obj = None
        if date := re.search(r"(([1-2][0-9])|([1-9])|(3[0-1]))/((1[0-2])|([1-9]))/[0-9]{4}", text):
           #TODO: if date is in dd/mm/yyyy form, you need to first switch it to
           # mm/dd/yyyy form

           #Convert regex obj to string
           date_str = date.group()    
           #Convert the string you found to datetime object
           date_obj=datetime.datetime.strptime(date_str, "%d/%m/%Y")
        else:
             print("Could not retrieve date")
             return   
        return date_obj

    def extractCreditCardNum(self, text:str) -> datetime:
            date_obj = None
            #TODO: change to credit card regex
            if date := re.search(r"(([1-2][0-9])|([1-9])|(3[0-1]))/((1[0-2])|([1-9]))/[0-9]{4}", text):
               #Convert regex obj to string
               date_str = date.group()    
               #Convert the string you found to datetime object
               date_obj=datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
               return date_obj