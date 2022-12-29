import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

page = requests.get(url)

data = BeautifulSoup(page.content, "html.parser")

text_chunks = data.find_all(class_="body__inner-container")

for text_chunk in text_chunks:
    print(text_chunk.text)
    print()