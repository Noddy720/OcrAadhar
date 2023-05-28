import cv2
import pytesseract

# Load image
img = cv2.imread('dhanesh.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform image thresholding to enhance text
threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Apply OCR using pytesseract
name = pytesseract.image_to_string(threshold, lang='eng', config='--psm 6')

print('Name:', name)