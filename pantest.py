import pytesseract
import re
from PIL import Image

# Load the image
img = Image.open('pan1.jpg')

# Extract text using OCR
text = pytesseract.image_to_string(img)

# Extract PAN number using regex
pan_number = re.search(r'[A-Z]{5}[0-9]{4}[A-Z]{1}', text)
if pan_number:
    pan_number = pan_number.group()
print('PAN number:', pan_number)

# Extract name using regex
name = re.findall(r'Name\n(.+)\n', text)
if name:
    name = name[0].strip()
print('Name:', name)

# Extract date of birth using regex
dob = re.findall(r'Date of Birth / Date of Incorporation(.+)', text)
if dob:
    dob = dob[0].strip().replace(' ', '')
print('Date of Birth / Incorporation:', dob)

# Extract father's name using regex
father_name = re.findall(r'FATHER.*\n(.+)\n', text)
if father_name:
    father_name = father_name[0].strip()
print("Father's Name:", father_name)

# # Extract address using regex
# address = re.findall(r'Address\n(.+)', text)
# if address:
#     address = address[0].strip()
# print('Address:', address)
