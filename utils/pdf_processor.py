from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_text_from_pdf(pdf_file):
    text = ""
    for pdf in pdf_file:
        pdf_reader = PdfReader(pdf)

        for page in pdf_reader.pages:
            extracted = page.extract_text()
            
            if extracted:
                text += "\n"

    return text

def create_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 10000,
        chunk_overlap = 1000
    )

    chunks = text_splitter.split_text(text)
    return chunks

