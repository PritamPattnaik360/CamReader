import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

camera = cv2.VideoCapture(0)

file = open("Record.txt", "w+")
file.write("")

while True:
    ret, image = camera.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    dilation = cv2.dilate(thresholded, rect_kernel, iterations = 1)
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            rect = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cropped = image[y:y + h, x:x + w]
            text = pytesseract.image_to_string(cropped)
            if len(text) > 0:
                print(text)
                file.write(text)
                file.write("\n")
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cv2.imshow('Camera', image)
    cv2.imshow('Proccessing', dilation)

file.close
camera.release()
cv2.destroyAllWindows()