from config import configure_logging, load_environment
from process import process_medical_information
from utils import create_directories, save_extracted_text, save_json, extract_text_from_pdf, converter_pdf_para_png_com_preprocessamento
from pathlib import Path
import logging

def process_single_pdf(pdf_file, txt_dir, json_dir, png_dir):
    base_name = pdf_file.stem
    try:
        # Diretório para salvar as imagens PNG
        #pdf_png_dir = png_dir / base_name
        
        # Converte o PDF em imagens PNG com pré-processamento
        #converter_pdf_para_png_com_preprocessamento(pdf_file, pdf_png_dir)
        
        # Extrai o texto do PDF
        extracted_text = extract_text_from_pdf(str(pdf_file))
        save_extracted_text(extracted_text, txt_dir / f"{base_name}.txt")

        # Processa as informações médicas
        structured_data = process_medical_information(extracted_text)
        save_json(structured_data, json_dir / f"{base_name}.json")

    except Exception as e:
        logging.error(f"Falha ao processar {pdf_file.name}: {e}")


def main():
    load_environment()
    configure_logging()
    
    logging.info("Iniciando a execução do script.")
    
    pdf_dir = Path('scans/pdf')
    txt_dir = Path('scans/txt')
    json_dir = Path('scans/json')
    png_dir = Path('scans/png')
    
    create_directories([pdf_dir, txt_dir, json_dir, png_dir])
    
    for pdf_file in pdf_dir.glob('*.pdf'):
        process_single_pdf(pdf_file, txt_dir, json_dir, png_dir)
    
    logging.info("Execução do script concluída.")


if __name__ == "__main__":
    main()
