import requests
from bs4 import BeautifulSoup

url = "https://www.nytimes.com/"

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

site_content = soup.find(class_="css-pqd7q9 eu3y8st0")

topics = site_content.find_all("h3")

file_name = input("Name the output file: ") + ".txt"
with open(file_name, 'w') as f:
    for topic in topics:
        f.write(topic.text.strip() + "\n")