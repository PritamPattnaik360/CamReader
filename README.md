# CamReader
## Description
The provided Python script employs the OpenCV and Tesseract libraries to perform real-time text extraction from a camera feed. Upon execution, it initializes video capture, continuously acquiring frames for processing. The script waits for user input to trigger text recognition by pressing the 's' key, identifying text regions using contour detection. OCR is then applied to extract textual content from these regions, with recognized text appended to a designated output file. The script provides visual feedback by displaying both the original camera feed and the processed image. User termination is facilitated by pressing the 'q' key, releasing the camera resource, and closing the output file.

##  Application in Action
### Screenshots
- The image below shows the raw feed of the camera.
<img width="500" alt="png1" src="https://github.com/PritamPattnaik360/CamReader/assets/37960218/36762914-c628-4424-99de-9dc651d866fc">

- The image is then processed.
<img width="500" alt="png2" src="https://github.com/PritamPattnaik360/CamReader/assets/37960218/a7474f74-7824-4202-b157-1f73051a2be4">

- The text region is identified and then scans for the word and retrieves it as a string.
<img width="500" alt="png3" src="https://github.com/PritamPattnaik360/CamReader/assets/37960218/650c98cb-6231-4431-bf4c-3c7d6b420622">

- Finally, the string is recorded and saved as a text file.
<img width="500" alt="png4" src="https://github.com/PritamPattnaik360/CamReader/assets/37960218/1225fe47-f33c-4156-a33e-fe9d3affe1a2">


## Dependencies 
```bash
pip install opencv-python
pip install pytesseract
```
You also need to download [Pytesseract-OCR](https://github.com/UB-Mannheim/tesseract/wiki)


