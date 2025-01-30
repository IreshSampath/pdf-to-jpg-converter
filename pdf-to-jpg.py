# open the terminal on the same folder & Run the below command
# python -m venv venv; .\venv\Scripts\Activate; pip install pdf2image; python pdf-to-jpg.py

import os
from pdf2image import convert_from_path
from pathlib import Path

script_dir = Path(__file__).parent  # Get the script's directory
poppler_path = script_dir / "poppler-24.08.0" / "Library" / "bin"
pdf_folder = script_dir / "PDF Files"
saving_folder = script_dir / "JPG Files"

def get_latest_pdf(folder):
    """Get the latest PDF file from the specified folder."""
    pdf_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.pdf')]
    if not pdf_files:
        raise FileNotFoundError("No PDF files found in the specified folder.")
    latest_pdf = max(pdf_files, key=os.path.getmtime)
    return latest_pdf

try:
    # Dynamically get the latest PDF file
    pdf_path = get_latest_pdf(pdf_folder)
    print(f"Processing file: {pdf_path}")

    # Convert PDF pages to images
    pages = convert_from_path(pdf_path=pdf_path, poppler_path=poppler_path)

    # Save images to the saving folder
    for c, page in enumerate(pages, start=1):
        img_name = f"img-{c}.jpeg"
        page.save(os.path.join(saving_folder, img_name), "JPEG")
        print(f"Saved {img_name} in {saving_folder}")

except Exception as e:
    print(f"Error: {e}")