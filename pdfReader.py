# Install required packages
# pip install PyPdf2

# Import required modues
import PyPDF2 as pdf

# Prompt user to upload pdf
input_file_path = input("Paste file path here: ") + ".pdf"

# Open the PDF file in binary read mode
file = open(input_file_path, "rb")

# Create reader object
pdf_reader = pdf.PdfReader(file)

# Accessing the pages of the PDF
pages_num = pdf_reader.pages

print(f"The PDF contains {pages_num} pages.")

for page_number in range(0, len(pdf_reader.pages)):
    page = pdf_reader.pages[page_number]
    page_content = page.extract_text()
    print(f"Page {page_number + 1}:")
    print(page_content)

file.close()