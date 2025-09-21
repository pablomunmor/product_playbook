import os
import faiss
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
from sentence_transformers import SentenceTransformer

# --- Initialization ---
app = Flask(__name__)
# Enable CORS to allow requests from the local HTML file, which is essential for local development.
CORS(app)

MODEL = None
INDEX = None
CHUNKS = None

def load_knowledge_base():
    """Loads the model, FAISS index, and text chunks into memory."""
    global MODEL, INDEX, CHUNKS
    print("Loading RAG model and knowledge base...")
    try:
        MODEL = SentenceTransformer('all-MiniLM-L6-v2')
        INDEX = faiss.read_index("knowledge_base.index")
        with open("knowledge_base_chunks.txt", "r", encoding="utf-8") as f:
            CHUNKS = [line.strip() for line in f.readlines()]
        print("Model and knowledge base loaded successfully.")
    except FileNotFoundError:
        print("\n\n---")
        print("ERROR: Knowledge base files (`knowledge_base.index`, `knowledge_base_chunks.txt`) not found.")
        print("Please ensure you have run `create_knowledge_base.py` from within the `backend` directory.")
        print("---\n\n")
        MODEL, INDEX, CHUNKS = None, None, None

# --- RAG Core Function ---
def search_knowledge_base(query, k=3):
    """Searches the knowledge base for the most relevant text chunks."""
    if not all([MODEL, INDEX, CHUNKS]):
        return ["Error: The knowledge base is not loaded. The AI Assistant is unavailable."]

    query_embedding = MODEL.encode([query]).astype('float32')
    distances, indices = INDEX.search(query_embedding, k)

    # Return the retrieved text chunks
    return [CHUNKS[i] for i in indices[0]]

# --- API Endpoint ---
@app.route('/api/chat', methods=['POST'])
def chat():
    """Handles the chat request, performs a RAG search, and returns the result."""
    if not all([MODEL, INDEX, CHUNks]):
        return jsonify({'response': "The AI assistant is currently unavailable because its knowledge base could not be loaded. Please check the server logs."}), 500

    data = request.get_json()
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'response': "Please provide a message in your request."}), 400

    # 1. Retrieve relevant context from the knowledge base
    relevant_chunks = search_knowledge_base(user_message)

    # 2. Simulate the "Generation" step of RAG
    # In a real-world system, this context would be fed to an LLM.
    # Here, we just present the retrieved information to the user.
    if relevant_chunks and "Error:" not in relevant_chunks[0]:
        response_intro = "Based on the playbook, here's some information that might help:\n"
        formatted_chunks = "\n\n---\n\n".join([f"• {chunk}" for chunk in relevant_chunks])
        response_message = response_intro + formatted_chunks
    else:
        response_message = "I couldn't find anything in the playbook that directly answers your question. Could you try rephrasing it?"

    return jsonify({'response': response_message})

if __name__ == '__main__':
    # Ensure the working directory is set to the script's location.
    # This allows the server to find the knowledge base files correctly.
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    load_knowledge_base()
    app.run(host='0.0.0.0', port=5001)
