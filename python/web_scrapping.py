from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-10gd/p" \
      "/N82E16814932459?Description=rtx%203080&cm_re=rtx_3080-_-14-932-459-_-Product"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)
