import scanner
import data_extractor

def main():
    s = scanner.Scanner()
    text = s.getCapturedText()
    #print("Text is " + text)
    
    d = data_extractor.DataExtractor()
    date = d.extractDate(text)

    if date:
        print(date)

    else:
        print("No date")
        return    
    return


if __name__=="__main__":
    main()