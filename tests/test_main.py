import logging
import os
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'src'))
from main_0 import process_medical_information
from utils import json_to_csv, json_to_unified_csv

def test_process_txt_to_json(txt_dir, json_dir):
    """Test the process of reading .txt, sending to chat, and saving output as .json."""

    # Ensure output directory exists
    os.makedirs(json_dir, exist_ok=True)

    # Iterate through all .txt files in the specified directory
    for txt_file in Path(txt_dir).glob("*.txt"):
        base_name = txt_file.stem  # Get the name without extension
        logging.info(f"Processing file: {txt_file}")

        try:
            # Read the content of the .txt file
            with open(txt_file, 'r', encoding='utf-8') as f:
                extracted_text = f.read()

            # Process the text to get structured data
            structured_data = process_medical_information(extracted_text)

            # Save the structured data to a .json file
            json_file = Path(json_dir) / f"{base_name}.json"
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(structured_data, f, ensure_ascii=False, indent=4)

            logging.info(f"Successfully processed and saved: {json_file}")

        except Exception as e:
            # Use logging.exception to log the full traceback of the exception
            logging.exception(f"Error processing {txt_file}")
        # Create a unified CSV after processing all JSON files

def test_process_json_to__unified_csv(json_dir):
    """Test the process of combining multiple JSON files into a single CSV file."""
    
    # Ensure output directory exists
    os.makedirs(json_dir, exist_ok=True)

    # Create a unified CSV file from all JSON files in the directory
    try:
        unified_csv_path = Path('scans/csv') / 'unified_data.csv'
        json_to_unified_csv(json_dir, unified_csv_path)
        logging.info(f"Unified CSV created at {unified_csv_path}")

    except Exception as e:
        # Use logging.exception to log the full traceback of the exception
        logging.exception(f"Error creating unified CSV file")

if __name__ == "__main__":
    # Define directories for testing
    txt_directory = 'scans/txt'
    json_output_directory = 'scans/json'

    # Run the test
    #test_process_txt_to_json(txt_directory, json_output_directory)
    test_process_json_to__unified_csv(json_output_directory)
