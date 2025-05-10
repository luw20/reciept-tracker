import pytest
import reciepttracker.reciept_tracker.scanner as scanner
from unittest.mock import patch

@pytest.fixture
def initialize_scanner():
    s = scanner.Scanner
    return s
    

def test_can_capture_text(initialize_scanner):
    s = initialize_scanner()
    assert isinstance(s.getCapturedText(""), str)

# Test if the program exits when 'q' is pressed
def test_exits_when_key_pressed(initialize_scanner):
    s = initialize_scanner()
    with patch('cv2.waitKey', side_effect=[ord('q')]):  # Simulate pressing 'q'
        result = s.captureTextFromVideo()
        assert result == ""  # Assuming no text is captured before exiting

if __name__ == '__main__':
    pytest.main()

