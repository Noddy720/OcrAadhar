import pytesseract
from PIL import Image

# Load the image
img = Image.open("dhanesh.jpg")

# Extract text using OCR
text = pytesseract.image_to_string(img)

# Extract name
name = ""
for line in text.split("\n"):
    if "Name" in line:
        name = line.split(":")[-1].strip()
        break
print("Name:", name)

# Extract gender
gender = ""
for line in text.split("\n"):
    if "Female" in line:
        gender = "Female"
        break
    elif "Male" in line:
        gender = "Male"
        break
print("Gender:", gender)

# Extract date of birth
dob = ""
for line in text.split("\n"):
    if "DOB" in line:
        dob = line.split(":")[-1].strip()
        break
print("Date of Birth:", dob)
