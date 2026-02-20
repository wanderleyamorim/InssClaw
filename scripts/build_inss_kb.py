import os
import argparse
import chromadb
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text

def main(docs_dir, db_dir):
    print(f"Iniciando escaneamento de PDFs em: {docs_dir}")
    if not os.path.exists(docs_dir):
        print(f"Diretório '{docs_dir}' não encontrado. Criando diretório vazio.")
        os.makedirs(docs_dir)
        print("Coloque suas portarias e INs em PDF lá e rode o script novamente.")
        return

    # Initialize ChromaDB persistent client
    client = chromadb.PersistentClient(path=db_dir)
    collection = client.get_or_create_collection(name="inss_kb")
    
    # Text splitter config: large chunks to keep context, overlap to avoid cutting sentences.
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=300
    )
    
    docs_to_insert = []
    metadatas = []
    ids = []
    
    for root, _, files in os.walk(docs_dir):
        for filename in files:
            if filename.lower().endswith(".pdf"):
                filepath = os.path.join(root, filename)
                print(f"Processando: {filepath}...")
                try:
                    text = extract_text(filepath)
                    chunks = splitter.split_text(text)
                    
                    for i, chunk in enumerate(chunks):
                        docs_to_insert.append(chunk)
                        metadatas.append({"source": filepath, "chunk": i})
                        ids.append(f"{filepath}_{i}")
                except Exception as e:
                    print(f"Erro ao ler {filepath}: {e}")
                
    if docs_to_insert:
        print(f"\nInserindo {len(docs_to_insert)} fragmentos de texto no banco de dados vetorial...")
        # ChromaDB handles generating embeddings automatically using default sentence-transformers model all-MiniLM-L6-v2
        collection.add(
            documents=docs_to_insert,
            metadatas=metadatas,
            ids=ids
        )
        print("Base de Conhecimento INSS atualizada com sucesso! Você já pode fazer perguntas.")
    else:
        print("Nenhum PDF processado ou nenhum texto extraído.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--docs", default="../pdfs", help="Pasta contendo as INs e Portarias em PDF")
    parser.add_argument("--db", default="../chroma_db", help="Pasta para salvar o banco de dados")
    args = parser.parse_args()
    
    # Resolve absolute paths based on script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    docs_abs = os.path.join(script_dir, args.docs)
    db_abs = os.path.join(script_dir, args.db)
    
    main(docs_abs, db_abs)
