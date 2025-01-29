from gemini import get_gemini_response

def perform_web_search(query):
    """Perform a web search using Gemini"""
    search_results = get_gemini_response(f"Search for: {query}")
    return search_results
