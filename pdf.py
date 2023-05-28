import os
import json
import tempfile
import fitz
from aadhar_utils import extract_aadhar_info

# Define the path to the PDF file
pdf_path = "/path/to/pdf_file.pdf"

# Initialize an empty list to store the extracted data
aadhar_data = []

# Open the PDF file
with fitz.open(pdf_path) as doc:
    # Iterate over each page in the PDF
    for page_num in range(doc.page_count): 
        # Get the page object
        page = doc[page_num]

        # Convert the page to a PIL image
        temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
        pix = page.get_pixmap(alpha=False)
        pix.writePNG(temp_file.name)
        img = Image.open(temp_file.name)

        # Extract the data from the image
        data = extract_aadhar_info(img)

        # Append the data to the list
        aadhar_data.append(data)

        # Close and delete the temporary file
        img.close()
        temp_file.close()
        os.unlink(temp_file.name)

# Save the data to a JSON file
with open("aadhar_data.json", "w") as f:
    json.dump(aadhar_data, f)