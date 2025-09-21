import os
import re
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

def get_file_contents():
    """Reads content from the project's text and HTML files."""
    filepaths = [
        "../main.html",
        "../IA.md",
        "../PRD.md",
        "../README.md",
        "../TECH_SPEC.md"
    ]
    docs = []
    for filepath in filepaths:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                # Store content along with its source file type
                docs.append({'content': content, 'source': os.path.basename(filepath)})
        except FileNotFoundError:
            print(f"Warning: File not found at {filepath}")
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
    return docs

def clean_text(text, source):
    """Cleans text, removing HTML tags and extra whitespace."""
    if source.endswith(".html"):
        # A simple but effective way to strip HTML for this specific file
        # Remove script and style blocks
        text = re.sub(r'<script.*?>.*?</script>', '', text, flags=re.DOTALL)
        text = re.sub(r'<style.*?>.*?</style>', '', text, flags=re.DOTALL)
        # Remove all other HTML tags
        text = re.sub(r'<.*?>', ' ', text)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def chunk_text(docs):
    """Splits documents into smaller, more manageable chunks."""
    chunks = []
    for doc in docs:
        clean_content = clean_text(doc['content'], doc['source'])
        # Split by paragraphs (double newline) or long lines of text
        paragraphs = re.split(r'\n\s*\n', clean_content)
        for p in paragraphs:
            p_stripped = p.strip()
            # Further split long paragraphs to respect model context limits
            if len(p_stripped) > 1000:
                sentences = re.split(r'(?<=[.!?])\s+', p_stripped)
                current_chunk = ""
                for sentence in sentences:
                    if len(current_chunk) + len(sentence) + 1 < 1000:
                        current_chunk += sentence + " "
                    else:
                        if len(current_chunk.strip()) > 50:
                            chunks.append(current_chunk.strip())
                        current_chunk = sentence + " "
                if len(current_chunk.strip()) > 50:
                     chunks.append(current_chunk.strip())
            elif len(p_stripped) > 50: # Only consider chunks with some substance
                chunks.append(p_stripped)
    return chunks

def main():
    """Main function to build and save the knowledge base."""
    print("Starting knowledge base creation...")

    # 1. Load and process documents
    print("Loading and chunking documents...")
    documents = get_file_contents()
    chunks = chunk_text(documents)

    if not chunks:
        print("No text chunks were created. Aborting.")
        return

    print(f"Successfully created {len(chunks)} text chunks.")

    # 2. Generate embeddings
    print("Loading sentence transformer model (all-MiniLM-L6-v2)...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("Creating embeddings for text chunks. This may take a moment...")
    embeddings = model.encode(chunks, show_progress_bar=True)
    embeddings = np.array(embeddings).astype('float32')

    # 3. Build and save the FAISS index
    print("Building and saving the FAISS index...")
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    faiss.write_index(index, 'knowledge_base.index')

    # 4. Save the corresponding text chunks
    # This is crucial because the index only stores vectors, not the text itself.
    with open('knowledge_base_chunks.txt', 'w', encoding='utf-8') as f:
        for chunk in chunks:
            # Replace newlines to ensure one chunk per line in the file
            f.write(chunk.replace('\n', ' ') + '\n')

    print("\nKnowledge base creation complete!")
    print("Files created in 'backend' directory:")
    print("- knowledge_base.index (FAISS vector store)")
    print("- knowledge_base_chunks.txt (The raw text for the vectors)")

if __name__ == '__main__':
    main()
