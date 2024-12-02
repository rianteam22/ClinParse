import json
from pdf2image import convert_from_path
import logging
from PIL import Image, ImageEnhance, ImageFilter
from pathlib import Path
from unstract.llmwhisperer.client import LLMWhispererClient, LLMWhispererClientException
import pandas as pd

def save_extracted_text(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    logging.info(f"Saved extracted text to {file_path}")

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    logging.info(f"Saved structured data to {file_path}")

def create_directories(paths):
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)

def extract_text_from_pdf(file_path, pages_list=None):
    llmw = LLMWhispererClient()
    try:
        result = llmw.whisper(file_path=file_path, pages_to_extract=pages_list)
        extracted_text = result["extracted_text"]
        logging.info(f"Extracted text from PDF: {file_path}")
        return extracted_text
    except LLMWhispererClientException as e:
        logging.error(f"Failed to extract text from PDF {file_path}: {e}")
        raise RuntimeError(f"Error extracting text from PDF {file_path}: {e}")
    except Exception as e:
        logging.exception(f"Unexpected error extracting text from PDF {file_path}: {e}")
        raise RuntimeError(f"Unexpected error extracting text from PDF {file_path}: {e}")
    
def converter_pdf_para_png_com_preprocessamento(pdf_path, output_dir):
    """
    Converte cada página de um PDF em imagens PNG, aplica pré-processamento para melhorar a qualidade do OCR
    e salva as imagens em um diretório específico.

    :param pdf_path: Caminho para o arquivo PDF.
    :param output_dir: Diretório onde as imagens PNG serão salvas.
    """
    try:
        # Converte o PDF em uma lista de imagens
        paginas = convert_from_path(pdf_path, dpi=400)
        
        # Cria o diretório de saída se não existir
        output_dir.mkdir(parents=True, exist_ok=True)
        
        for i, pagina in enumerate(paginas):
            # Converte para escala de cinza
            imagem = pagina.convert('L')
            
            # Aumenta o contraste
            enhancer = ImageEnhance.Sharpness(imagem)
            imagem = enhancer.enhance(1.0)  # Ajuste o fator conforme necessário
            
            # Aplica filtro de nitidez
            imagem = imagem.filter(ImageFilter.DETAIL)
            
            # Binariza a imagem
            imagem = imagem.point(lambda x: 0 if x < 128 else 255, '1')
            
            # Salva a imagem processada como PNG
            imagem_path = output_dir / f"pagina_{i + 1}.png"
            imagem.save(imagem_path, 'PNG')
            logging.info(f"Página {i + 1} salva como {imagem_path}")
    
    except Exception as e:
        logging.error(f"Erro ao converter {pdf_path} para imagens PNG: {e}")


def json_to_csv(json_file_path, csv_file_path):
    """
    Converts a JSON file to a CSV DataFrame and saves it to a specified CSV file path.

    Args:
        json_file_path (str or Path): The path to the JSON file.
        csv_file_path (str or Path): The path to save the CSV file.
    """
    try:
        # Load the JSON data
        with open(json_file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        # Convert the JSON data to a DataFrame
        df = pd.json_normalize(json_data)
        
        # Save the DataFrame to a CSV file
        df.to_csv(csv_file_path, index=False, encoding='utf-8')
        logging.info(f"Successfully converted {json_file_path} to {csv_file_path}")

    except Exception as e:
        logging.error(f"Failed to convert {json_file_path} to CSV: {e}")
        raise

def json_to_unified_csv(json_dir, unified_csv_path):
    """
    Combines multiple JSON files in a directory into a single CSV file.

    Args:
        json_dir (str or Path): Directory containing the JSON files.
        unified_csv_path (str or Path): Path where the unified CSV file will be saved.
    """
    try:
        # List to store each DataFrame
        dataframes = []

        # Iterate through all .json files in the specified directory
        for json_file in Path(json_dir).glob("*.json"):
            with open(json_file, 'r', encoding='utf-8') as f:
                json_data = json.load(f)

            # Convert the JSON data to a DataFrame
            df = pd.json_normalize(json_data)
            dataframes.append(df)

        # Concatenate all DataFrames into a single DataFrame
        unified_df = pd.concat(dataframes, ignore_index=True)

        # Save the unified DataFrame to a CSV file
        unified_df.to_csv(unified_csv_path, index=False, encoding='utf-8')
        logging.info(f"Unified CSV file created at {unified_csv_path}")

    except Exception as e:
        logging.error(f"Failed to create unified CSV file: {e}")
        raise