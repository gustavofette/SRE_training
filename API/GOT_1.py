import requests
import json

root_url = "https://www.anapioficeandfire.com/api"
characters_url = "https://www.anapioficeandfire.com/api/characters"
houses_url = "https://www.anapioficeandfire.com/api/houses"
books_url = "https://www.anapioficeandfire.com/api/books"

char_name = input("Please choose your character:")
char_response = requests.get(characters_url, params={"q": char_name})
print (char_response.json())

