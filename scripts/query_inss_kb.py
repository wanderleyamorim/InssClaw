import os
import argparse
import chromadb

def query_kb(query_text, db_dir, n_results):
    if not os.path.exists(db_dir):
        print(f"Banco de dados não encontrado em {db_dir}.")
        print("Rode build_inss_kb.py para criar a base primeiro antes de fazer consultas.")
        return

    # Connect to the persistent database
    client = chromadb.PersistentClient(path=db_dir)
    try:
        collection = client.get_collection(name="inss_kb")
    except Exception:
        print("Coleção 'inss_kb' não encontrada. O banco parece estar vazio.")
        return
        
    print(f"Buscando pelas leis mais relevantes para: '{query_text}'...")
    
    # Query the collection
    results = collection.query(
        query_texts=[query_text],
        n_results=n_results
    )
    
    docs = results.get('documents', [[]])[0]
    metas = results.get('metadatas', [[]])[0]
    
    if not docs:
        print("Nenhum resultado relevante encontrado.")
        return
        
    print("\n" + "="*70)
    print(" RESULTADOS DA BUSCA NA BASE DE CONHECIMENTO DO INSS ".center(70))
    print("="*70)
    
    for i, (doc, meta) in enumerate(zip(docs, metas)):
        print(f"\n[ Resultado {i+1} | Fonte: {meta['source']} | Fragmento {meta['chunk']} ]")
        print("-" * 70)
        print(doc.strip())
        print("-" * 70)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="A sua dúvida ou termo de busca (ex: 'aposentadoria tempo de contribuição especial')")
    parser.add_argument("--db", default="../chroma_db", help="Pasta do banco de dados vetorial")
    parser.add_argument("--n", type=int, default=3, help="Número máximo de parágrafos de leis para retornar")
    args = parser.parse_args()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    db_abs = os.path.join(script_dir, args.db)
    
    query_kb(args.query, db_abs, args.n)
