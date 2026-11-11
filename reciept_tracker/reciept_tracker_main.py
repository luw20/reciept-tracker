import scanner
import data_extractor
import datetime

def main():
    s = scanner.Scanner()
    text = s.getCapturedText()
    #print("Text is " + text)
    
    d = data_extractor.DataExtractor()
    date = d.extractDate("string is 11/12/1996")

    if date:
        extracted_date_str = date.strftime("%d/%m/%Y")
        print("extracted date is:" + extracted_date_str)
    else:
        print("No date")
        return    
    return


if __name__=="__main__":
    main()