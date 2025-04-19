import azure.functions as func
from azure.functions import AuthLevel
import logging

app = func.FunctionApp()

@app.function_name(name="chat")
@app.route(route="chat", auth_level=AuthLevel.ANONYMOUS)
def chat(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Chat endpoint called")
    return func.HttpResponse("Chat endpoint hit!", status_code=200)

@app.function_name(name="load_chat")
@app.route(route="load-chat", auth_level=AuthLevel.ANONYMOUS)
def load_chat(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Load Chat endpoint called")
    return func.HttpResponse("Load chat endpoint hit!", status_code=200)

@app.function_name(name="save_chat")
@app.route(route="save-chat", auth_level=AuthLevel.ANONYMOUS)
def save_chat(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Save Chat endpoint called")
    return func.HttpResponse("Save chat endpoint hit!", status_code=200)

@app.function_name(name="delete_chat")
@app.route(route="delete-chat", auth_level=AuthLevel.ANONYMOUS)
def delete_chat(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Delete Chat endpoint called")
    return func.HttpResponse("Delete chat endpoint hit!", status_code=200)

@app.function_name(name="rag_chat")
@app.route(route="rag-chat", auth_level=AuthLevel.ANONYMOUS)
def rag_chat(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("RAG Chat endpoint called")
    return func.HttpResponse("RAG chat endpoint hit!", status_code=200)

@app.function_name(name="upload_pdf")
@app.route(route="upload-pdf", auth_level=AuthLevel.ANONYMOUS)
def upload_pdf(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Upload PDF endpoint called")
    return func.HttpResponse("Upload PDF endpoint hit!", status_code=200)