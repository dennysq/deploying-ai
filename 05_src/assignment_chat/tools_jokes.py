from langchain.tools import tool
import json
import requests


@tool
def get_joke():
    """
    Returns a joke from the JokeAPI.
    """
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
   
    response = requests.get(url)
    resp_dict = json.loads(response.text)
    joke = resp_dict.get("joke", "")
    return joke

