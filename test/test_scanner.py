import pytest
import reciepttracker.reciept_tracker.scanner as scanner

@pytest.fixture
def initialize_scanner():
    s = scanner.Scanner
    return s
    

def test_can_capture_text(initialize_scanner):
    s = initialize_scanner()
    assert isinstance(s.getCapturedText(""), str)

if __name__ == '__main__':
    pytest.main()

