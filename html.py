import requests

def load_html(source: str) -> str:

    """
    Fetch HTML content from a URL

    Parameters:
    source (str): URL or file path to fetch HTML content from.

    Returns:
    str: The HTML content as a string. 
    """

    if not isinstance(source, str) or not source.strip():
        raise TypeError("Source must be a non-empty string.")
    if source.startswith(('http://', 'https://')):
        response = requests.get(source, timeout = 200)
        response.raise_for_status()  # Raise an error for bad responses
        return response.text
    
