from paddleocr import PaddleOCR

# Initialize PaddleOCR
# Specify the language for text recognition (e.g., English)
# You might need to adjust this for other languages or layouts
ocr = PaddleOCR(use_angle_classifier=True, lang='en')

# Define the image path
img_path = './book_of_proof_page_3.png'

# Perform OCR, which includes layout analysis
result = ocr.ocr(img_path, cls=True)

# Process the results to extract layout information
# The 'result' variable will contain a list of detected text lines
# with their bounding boxes and recognized text.
# You can then use this information to identify structural elements.
for line in result:
    print(line) # This will print details for each detected text line
    line.save_to_json('/output')

# For specific document parsing features like tables, use the pp_structure function
# from the CLI (as shown in step 2), as the SDK integration for PP-Structure
# might be more involved and require specific module imports or functions
# depending on the PaddleOCR version.
