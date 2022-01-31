from bs4 import BeautifulSoup
import requests
import re

gpu = input("What gpu are you looking for? ")
url = f"https://www.newegg.com/p/pl?d={gpu}&N=4131"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])
print(pages)
