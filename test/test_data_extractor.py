import pytest
import datetime
import reciepttracker.reciept_tracker.data_extractor as data_extractor
from unittest.mock import patch

@pytest.fixture
def initialize_data_extractor():
    d = data_extractor.DataExtractor
    return d
    

def test_can_extract_date(initialize_data_extractor):
    text = "here is a date 11/13/1996"
    d = initialize_data_extractor()
    date = d.extractDate(text)
    print(date)

    date_obj = datetime.datetime.strptime(date, "%m/%d/%Y")
    assert isinstance(date_obj, datetime.datetime)

if __name__ == '__main__':
    pytest.main()    

