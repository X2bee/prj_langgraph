import os
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

with open('API_KEY.txt', 'r') as api:
    os.environ["OPENAI_API_KEY"] = api.read()
    
urls = [
    "https://the-edit.co.kr/65111",
    "https://blog.naver.com/sud_inc/223539001961?trackingCode=rss",
    "https://mochaclass.com/blog/직장인을-위한-취미생활-가이드-요즘-취미-트렌드부터-취미-추천까지-7797",
    "https://www.hankyung.com/article/2024072845441",
]

docs = [WebBaseLoader(url).load() for url in urls]
docs_list = [item for sublist in docs for item in sublist]

text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=100, chunk_overlap=50
)
doc_splits = text_splitter.split_documents(docs_list)

# Add to vectorDB
vectorstore = Chroma.from_documents(
    documents=doc_splits,
    collection_name="rag-chroma",
    embedding=OpenAIEmbeddings(),
    persist_directory="./chroma_db",
)

vectorstore.persist("./chroma_data")