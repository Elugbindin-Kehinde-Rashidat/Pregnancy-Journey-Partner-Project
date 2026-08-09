import os
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer
from google import genai
from dotenv import load_dotenv


# ============================================
# Load environment variables
# ============================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

load_dotenv(PROJECT_ROOT / ".env")


# ============================================
# Connect to ChromaDB
# ============================================

VECTOR_DB_PATH = PROJECT_ROOT / "chatbot" / "knowledge_base" / "vector_db"

chroma_client = chromadb.PersistentClient(
    path=str(VECTOR_DB_PATH)
)

collection = chroma_client.get_collection(
    "pregnancy_knowledge"
)


# ============================================
# Load embedding model
# ============================================

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


# ============================================
# Connect to Gemini
# ============================================

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ============================================
# Retrieve relevant knowledge
# ============================================

def retrieve_context(question, n_results=5):

    embedding = embedding_model.encode(
        question,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    results = collection.query(
        query_embeddings=[embedding.tolist()],
        n_results=n_results
    )

    return results


# ============================================
# Build source-aware context
# ============================================

def build_source_aware_context(results):

    context_parts = []

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    for i, (document, metadata) in enumerate(
        zip(documents, metadatas),
        start=1
    ):

        organization = metadata.get(
            "organization",
            "Unknown"
        )

        document_name = metadata.get(
            "document",
            "Unknown"
        )

        page_number = metadata.get(
            "page_number",
            "Unknown"
        )

        title = metadata.get(
            "title",
            "Unknown"
        )

        url = metadata.get(
            "url",
            ""
        )

        context_parts.append(
            f"""
SOURCE {i}

Organization: {organization}
Document: {document_name}
Page: {page_number}
Title: {title}
URL: {url}

Content:
{document}
"""
        )

    return "\n".join(context_parts)


# ============================================
# RAG prompt
# ============================================

def build_rag_prompt(question, context):

    return f"""
You are Pregnancy Journey Partner, an educational pregnancy
information assistant.

Your role is to provide clear, simple, supportive and evidence-based
pregnancy information using ONLY the trusted knowledge provided in
the retrieved context.

IMPORTANT RULES:

1. Use the retrieved context as your primary source of information.

2. Do not invent medical facts, recommendations, medications,
diagnoses, or treatment instructions that are not supported by
the retrieved context.

3. If the retrieved context does not contain enough information to
answer a question, clearly say that the available knowledge base
does not contain enough information rather than making up an answer.

4. For urgent symptoms or danger signs, clearly encourage the user
to seek appropriate medical care promptly.

5. Do not diagnose the user or claim to replace a doctor, midwife,
nurse, or other healthcare professional.

6. Give simple and easy-to-understand answers.

7. When possible, mention the organization and source document
supporting the answer.

8. Do not mention information that is not supported by the retrieved
context.

MEDICAL DISCLAIMER:

Pregnancy Journey Partner provides general educational information
and is not a substitute for professional medical advice, diagnosis,
or treatment.

RETRIEVED CONTEXT:
{context}

USER QUESTION:
{question}

ANSWER:
"""


# ============================================
# Generate RAG answer
# ============================================

def generate_answer(question, n_results=5):

    results = retrieve_context(
        question,
        n_results=n_results
    )

    context = build_source_aware_context(
        results
    )

    prompt = build_rag_prompt(
        question,
        context
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text