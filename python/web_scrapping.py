from bs4 import BeautifulSoup
import requests
import re

gpu = input("What gpu are you looking for? ")
url = f"https://www.newegg.com/p/pl?d={gpu}&N=4131"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])

all_items = {}

for page in range(1, pages + 1):
    url = f"https://www.newegg.ca/p/pl?d={gpu}&N=4131&page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    div = doc.find(class_="item-cells-wrap border-cells items-grid-view four-cells expulsion-one-cell")

    find_items = div.find_all(text=re.compile(gpu))
    for item in find_items:
        parent = item.parent
        if parent.name != "a":
            continue

        link = parent["href"]
        next_parent = item.find_parent(class_="item-container")
        try:
            price = next_parent.find(class_="price-current").find("strong").string
            all_items[item] = {"price": int(price.replace(",", "")), "link": link}
        except:
            print("Could not find price.")

sorted_items = sorted(all_items.items(), key=lambda x: x[1]['price'])

for item in sorted_items:
    print(item[0])
    print(f"${item[1]['price']}")
    print(item[1]['link'])
    print("-------------------------------")
