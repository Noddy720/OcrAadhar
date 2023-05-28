import pytesseract
import re
from PIL import Image

def extract_aadhar_info(image_path):
    # Load the image
    img = Image.open(image_path)

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
        name = name_match.group(0).strip()

    # Extract gender using regular expressions
    gender_regex = re.compile(r"(Female|Male|Transgender)")
    gender_match = gender_regex.search(text)

    if gender_match is None:
        gender = ""
    else:
        gender = gender_match.group(0)

    # Extract date of birth using regular expressions
    # dob_regex = re.compile(r"DOB|dob|DoB|d.o.b|D.O.B|dobt|DOBt|d-o-b|D-O-B|dob\*")
    # dob_match = dob_regex.search(text)

    # if dob_match is None:
    #     dob = ""
    # else:
    #     dob_text = dob_match.string[dob_match.end():dob_match.end()+10]
    #     dob_regex2 = re.compile(r"\d{2}\/\d{2}\/\d{4}")
    #     dob_match2 = dob_regex2.search(dob_text)
    #     if dob_match2 is None:
    #         dob = ""
    #     else:
    #         dob = dob_match2.group(0)

    dob = ""
    for line in text.split("\n"):
        if "DOB" in line:
            dob = line.split(":")[-1].strip()
            break
    print("Date of Birth:", dob)


    # Print the Aadhar number, name, gender, and date of birth
    print("Aadhar Number: ", aadhar_number[0])
    print("Name: ", name)
    print("Gender: ", gender)
    print("Date of Birth: ", dob)

    return {
        "aadhar_number": aadhar_number,
        "name": name,
        "gender": gender,
        "dob": dob,
        
        
    }

