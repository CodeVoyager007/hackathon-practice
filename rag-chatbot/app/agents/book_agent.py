from openai import OpenAI
from qdrant_client import QdrantClient
from app.core.config import settings
from app.core.guardrails import InputGuardrail, OutputGuardrail

COLLECTION_NAME = "book_vectors"

def get_qdrant_client():
    """
    Returns an authenticated Qdrant client.
    """
    return QdrantClient(
        url=settings.QDRANT_URL, 
        api_key=settings.QDRANT_API_KEY,
    )

def get_gemini_client():
    """
    Returns an authenticated Gemini client via OpenAI SDK wrapper.
    """
    return OpenAI(
        api_key=settings.GEMINI_API_KEY,
        base_url="https://generativelanguage.googleapis.com/v1beta",
        http_client=None, # Workaround for a potential httpx proxy issue
    )

def retrieval_tool(question: str) -> dict:
    """
    Queries the Qdrant database for relevant document chunks based on the question
    and returns the concatenated content and sources.
    """
    qdrant_client = get_qdrant_client()
    gemini_client = get_gemini_client()

    # Embed the question
    response = gemini_client.embeddings.create(
        model="models/embedding-001",
        input=question
    )
    query_vector = response.data[0].embedding

    # Search for relevant chunks
    search_result = qdrant_client.search(
        collection_name=COLLECTION_NAME,
        query_vector=query_vector,
        limit=5,
    )

    # Concatenate the content and gather sources
    context = ""
    sources = []
    for result in search_result:
        context += result.payload["text"] + "\n\n"
        if "Header 1" in result.payload["metadata"]:
            sources.append(result.payload["metadata"]["Header 1"])

    return {"context": context, "sources": list(set(sources))}

def direct_qa_tool(question: str, context_text: str) -> dict:
    """
    Uses the provided context_text to answer the question.
    """
    # This tool doesn't need to query Qdrant. It uses the context directly.
    return {"context": context_text, "sources": ["User-provided text"]}


class BookAgent:
    """
    The agent responsible for handling user questions about the book.

    This agent can operate in two modes:
    1. General Retrieval: Answers questions based on the entire book's content.
    2. Context-Only: Answers questions based only on a user-provided text snippet.
    """
    def __init__(self):
        """
        Initializes the BookAgent with a Gemini client and guardrails.
        """
        self.gemini_client = get_gemini_client()
        self.input_guardrail = InputGuardrail()
        self.output_guardrail = OutputGuardrail()

    def run(self, question: str, context_text: str = None) -> dict:
        """
        Runs the agent to get an answer for the given question.

        Args:
            question: The user's question.
            context_text: Optional. If provided, the agent will only use this text
                          as context to answer the question.

        Returns:
            A dictionary containing the answer and the sources used.
        """
        if not self.input_guardrail.check(question):
            return {"answer": "Your question appears to contain malicious content. Please rephrase.", "sources": []}

        if context_text:
            retrieval_result = direct_qa_tool(question, context_text)
            prompt_template = """Please answer the question based ONLY on the following text. 
If the answer is not in the text, say 'I cannot find the answer in the provided text.'

Context:
{context}

Question: {question}

Answer:"""
        else:
            retrieval_result = retrieval_tool(question)
            prompt_template = """Based on the following context from the book, please answer the question.

Context:
{context}

Question: {question}

Answer:"""

        context = retrieval_result["context"]
        sources = retrieval_result["sources"]

        if not context:
            return {"answer": "I could not find any information on this topic in the book.", "sources": []}

        # Format the prompt
        prompt = prompt_template.format(context=context, question=question)

        # Call the Gemini LLM
        response = self.gemini_client.completions.create(
            model="models/gemini-1.5-flash-latest",
            prompt=prompt,
            max_tokens=500,
        )

        raw_answer = response.choices[0].text.strip()
        
        # Apply output guardrail
        safe_answer = self.output_guardrail.check(raw_answer)
        final_answer = self.output_guardrail.add_citations(safe_answer, sources)

        return {"answer": final_answer, "sources": sources}
