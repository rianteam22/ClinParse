import json
import logging
from pdf2image import convert_from_path
from PIL import Image, ImageEnhance, ImageFilter
from pathlib import Path
import pandas as pd
from unstract.llmwhisperer.client_v2 import LLMWhispererClientException
from unstract.llmwhisperer import LLMWhispererClientV2

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
    llmw = LLMWhispererClientV2()
    try:
        result = llmw.whisper(
            wait_for_completion=True,
            wait_timeout=200,
            file_path=file_path, 
            pages_to_extract=pages_list
        )
        extracted_text = result["extraction"]["result_text"]
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
    Converte um arquivo JSON para um DataFrame CSV e o salva no caminho especificado.

    :param json_file_path: Caminho para o arquivo JSON.
    :param csv_file_path: Caminho onde o arquivo CSV será salvo.
    """
    try:
        # Carrega os dados do JSON
        with open(json_file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        # Converte os dados JSON para um DataFrame
        df = pd.json_normalize(json_data)
        
        # Salva o DataFrame em um arquivo CSV
        df.to_csv(csv_file_path, index=False, encoding='utf-8')
        logging.info(f"Successfully converted {json_file_path} to {csv_file_path}")

    except Exception as e:
        logging.error(f"Failed to convert {json_file_path} to CSV: {e}")
        raise

def json_to_unified_csv(json_dir, unified_csv_path):
    """
    Combina múltiplos arquivos JSON em um diretório em um único arquivo CSV.

    :param json_dir: Diretório contendo os arquivos JSON.
    :param unified_csv_path: Caminho onde o arquivo CSV unificado será salvo.
    """
    try:
        # Lista para armazenar cada DataFrame
        dataframes = []

        # Itera por todos os arquivos .json no diretório especificado
        for json_file in Path(json_dir).glob("*.json"):
            with open(json_file, 'r', encoding='utf-8') as f:
                json_data = json.load(f)

            # Converte os dados JSON para um DataFrame
            df = pd.json_normalize(json_data)
            dataframes.append(df)

        # Concatena todos os DataFrames em um único DataFrame
        unified_df = pd.concat(dataframes, ignore_index=True)

        # Salva o DataFrame unificado em um arquivo CSV
        unified_df.to_csv(unified_csv_path, index=False, encoding='utf-8')
        logging.info(f"Unified CSV file created at {unified_csv_path}")

    except Exception as e:
        logging.error(f"Failed to create unified CSV file: {e}")
        raise
