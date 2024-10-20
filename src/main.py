from config import configure_logging, load_environment
from process import process_medical_information
from utils import create_directories, save_extracted_text, save_json, extract_text_from_pdf
from pathlib import Path
import logging

def process_single_pdf(pdf_file, txt_dir, json_dir):
    base_name = pdf_file.stem
    try:
        # Placeholder for the PDF text extraction function
        extracted_text = extract_text_from_pdf(str(pdf_file))
        save_extracted_text(extracted_text, txt_dir / f"{base_name}.txt")

        structured_data = process_medical_information(extracted_text)
        save_json(structured_data, json_dir / f"{base_name}.json")

    except Exception as e:
        logging.error(f"Failed to process {pdf_file.name}: {e}")

def main():
    load_environment()
    configure_logging()
    
    logging.info("Starting the script execution.")
    
    pdf_dir = Path('scans/pdf')
    txt_dir = Path('scans/txt')
    json_dir = Path('scans/json')
    
    create_directories([pdf_dir, txt_dir, json_dir])
    
    for pdf_file in pdf_dir.glob('*.pdf'):
        process_single_pdf(pdf_file, txt_dir, json_dir)
    
    logging.info("Script execution completed.")

if __name__ == "__main__":
    main()
