# CamReader
## Description
The provided Python script employs the OpenCV and Tesseract libraries to perform real-time text extraction from a camera feed. Upon execution, it initializes video capture, continuously acquiring frames for processing. The script waits for user input to trigger text recognition by pressing the 's' key, identifying text regions using contour detection. OCR is then applied to extract textual content from these regions, with recognized text appended to a designated output file. The script provides visual feedback by displaying both the original camera feed and the processed image. User termination is facilitated by pressing the 'q' key, releasing the camera resource, and closing the output file.

## Dependencies 
```bash
pip install opencv-python
pip install pytesseract
```
You also need to download [Pytesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)
##  Application in Action
### coming soon


