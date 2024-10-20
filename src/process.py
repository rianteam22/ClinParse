from models import FormDoc  # Assuming FormDoc contains all the nested models
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_openai import ChatOpenAI
import logging
import json
import re

def clean_and_parse_response(response_text):
    cleaned_text = re.sub(r"```json|```", "", response_text).strip()
    try:
        return json.loads(cleaned_text)
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse JSON data: {e}")
        return None

def process_medical_information(extracted_text):
    preamble = ("You are provided with text extracted from a medical" +
                "form, which contains various data fields related to patient" + 
                "information, diagnoses, treatments, and outcomes." +
                "Your task is to analyze this text and extract relevant data" +
                "into a structured JSON format that matches the predefined schema." + 
                "Ensure that only valid JSON is returned, with all fields populated" +
                "according to the extracted information. Use null for any missing" + 
                "data.")
    postamble = ("Only return the JSON data in a structured format" +
                 "that matches the schema. Do not include any additional" +
                 "text, comments, or explanations")

    system_template = "{preamble}"
    human_template = "{format_instructions}\n\nExtracted Text:\n{extracted_text}\n\n{postamble}"
    
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    parser = PydanticOutputParser(pydantic_object=FormDoc)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    
    request = chat_prompt.format_prompt(
        preamble=preamble,
        format_instructions=parser.get_format_instructions(),
        extracted_text=extracted_text,
        postamble=postamble
    ).to_messages()

    chat = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

    try:
        response = chat.invoke(request)
        return clean_and_parse_response(response.content)
    except Exception as e:
        logging.exception(f"Error processing medical information: {e}")
        raise RuntimeError("Error processing medical information.")
