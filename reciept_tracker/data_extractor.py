import datetime
import re

class DataExtractor:
    def __init__(self, data = ""):
         self.data = data


    def extractDate(self, text:str) -> str:
        date_str =""
        if two_digit_date := re.search(r"(\d{2})\/(\d{2})\/(\d{2})", text):
           
           if four_digit_date := re.search(r"(\d{2}[\/-]\d{2}[\/-]\d{4}|\d{4}[\/-]\d{2}[\/-]\d{2})", text):
              date_str = four_digit_date.group()
              print(date_str)
              return date_str  
           
           else:
             date_str = two_digit_date.group()
             print(date_str)
             return date_str
             
        else: print("Could not retrieve date")
        return   

    def extractCreditCardNum(self, text:str) -> datetime:
            date_obj = None
            #TODO: change to credit card regex
            if date := re.search(r"(([1-2][0-9])|([1-9])|(3[0-1]))/((1[0-2])|([1-9]))/[0-9]{4}", text):
               #Convert regex obj to string
               date_str = date.group()    
               #Convert the string you found to datetime object
               date_obj=datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
               return date_obj