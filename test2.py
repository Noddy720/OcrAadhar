import re
import pytesseract
from PIL import Image

# Load the image
img = Image.open("dhanesh.jpg")

# Extract text using OCR
text = pytesseract.image_to_string(img)

# Extract date of birth using regular expressions
dob_regex = r"DOB\n(\d{2}\-\w{3}\-\d{4})"
matches = re.search(dob_regex, text)
if matches:
    dob = matches.group(1).replace("-", "/")
    print("DOB:", dob)
else:
    print("DOB not found")
