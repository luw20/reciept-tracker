# Import required packages
import cv2
import pytesseract

class Scanner:
    def __init__(self, text = ""):
         self.text = text

    def captureTextFromVideo(self):    
         # Mention the installed location of Tesseract-OCR in your system
         pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
         
         # Initialize the video capture
         cap = cv2.VideoCapture(0)  # 0 for the default camera
         cap.set(3, 640)
         cap.set(4, 480)
         
         try:
             while True:
                 # Read a frame from the camera
                 ret, frame = cap.read()
                 if not ret:
                     print("Failed to capture frame. Exiting...")
                     break
                 
                 # Perform OCR on the frame
                 self.text = pytesseract.image_to_string(frame)
                 
                 # Perform bounding box detection using Tesseract's built-in capabilities
                 d = pytesseract.image_to_data(frame, output_type=pytesseract.Output.DICT)
                 n_boxes = len(d['text'])
                 for i in range(n_boxes):
                     if int(float(d['conf'][i])) > 0:
                         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                         frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                         
                 # Display the frame and the recognized text
                 cv2.imshow('Camera', frame)
                 print("Capturing...")
                 print(self.text)
                 
                 # Exit if 'q' is pressed
                 if cv2.waitKey(1) & 0xFF == ord('q'):
                     print("Exiting...")
                     break
         except KeyboardInterrupt:
             print("KeyboardInterrupt detected. Exiting gracefully...")
         finally:
             # Release the video capture and close the window
             cap.release()
             cv2.destroyAllWindows()
             return self.text
    
    def getCapturedText(self, captured_text = ""):
        captured_text = self.captureTextFromVideo()
        return captured_text





