#to extract content from PDF files
import fitz #it is the package name for PyMuPDF, which is a Python binding for the MuPDF library, used for handling PDF files.
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
os.environ["OPENROUTER_API_KEY"] = OPENROUTER_API_KEY


client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY
)#client is an instance of the OpenAI class, which is used to interact with the OpenAI API. The api_key parameter is set to the value of OPENROUTER_API_KEY, which is retrieved from the environment variables using os.getenv().


def extract_text_from_pdf(uploaded_file):
    """Extracts text from a PDF file.
    
    Args:
        uploaded_file: The uploaded PDF file object.
    
    Returns:
    str: The extracted text from the PDF file.
    
    """
   
    doc=fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text=""#initialize an empty string to store the extracted text
    for page in doc:
        text+=page.get_text()   
    return text



def ask_openai(prompt,max_tokens=800 ):
    """Sends a prompt to the OpenAI API and returns the response.
    
    Args:
        prompt: The prompt to send to the OpenAI API.
        max_tokens: The maximum number of tokens to generate in the response.
"""
    response=client.chat.completions.create(
        model="openai/gpt-oss-120b:free",
        messages=[
            {"role":"user",
             "content":prompt
            }
          ],
        max_tokens=max_tokens,
        temperature=0.8
    )
    return response.choices[0].message.content

















