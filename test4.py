import pytesseract
import re
from fuzzywuzzy import process
from PIL import Image

# Load the image
img = Image.open('dhanesh.jpg')

# Set tesseract parameters
custom_config = r'--oem 3 --psm 6'

# Extract text using OCR
text = pytesseract.image_to_string(img, config=custom_config)
text1 = pytesseract.image_to_string(img)

# Extract Aadhar number using regular expressions
aadhar_number = re.findall(r'\d{4}\s\d{4}\s\d{4}', text1)

# Extract name using regular expressions
name_regex = re.compile(r'(?i)([a-z]+\s)+[a-z]+')
name_match = name_regex.search(text)

if name_match is None:
    name = ""
else:
    # Use fuzzy string matching to find the closest match to the extracted name
    extracted_name = name_match.group(0).strip()
    names_to_match = ['first name', 'middle name', 'last name']
    closest_match = process.extractOne(extracted_name, names_to_match)
    if closest_match[1] >= 80:
        name = closest_match[0] + ': ' + extracted_name
    else:
        name = ""

# Extract gender using regular expressions
gender_regex = re.compile(r"(Female|Male|Transgender)")
gender_match = gender_regex.search(text)

if gender_match is None:
    gender = ""
else:
    gender = gender_match.group(0)

# Extract date of birth using regular expressions
dob_regex = re.compile(r"(DOB|D.O.B|Birth|Date of Birth)[\s\n]*([\d/]+)")
dob_match = dob_regex.search(text)

if dob_match is None:
    dob = ""
else:
    dob = dob_match.group(2).strip()

# Print the Aadhar number, name, gender, and date of birth
print("Aadhar Number: ", aadhar_number[0])
print("Name: ", name)
print("Gender: ", gender)
print("Date of Birth: ", dob)