from langchain.tools import tool
import json
import requests


@tool
def get_fact():
    """
    Returns a fact from useless facts API.
    """
    url = "https://uselessfacts.jsph.pl//api/v2/facts/random"
    
    response = requests.get(url)
    resp_dict = json.loads(response.text)
    fact = resp_dict.get("text", "")
    return fact

