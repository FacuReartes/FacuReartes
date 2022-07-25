from bs4 import BeautifulSoup
import requests
import pandas as pd

"""
university
POStal
website
mail
phone
fax
"""

url = "https://americassbdc.org/about-us/state-directors/"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
chapters = soup.find_all("p")
chapter = soup.find("p")
master_list = []


for i in chapters:
    data_dict = {}
    nextsibling = a_tag = None
    tax = "There is no fax"
    a_tag = i.find_all("a")
    if len(a_tag) > 1 and "@" in a_tag[0].text:
        data_dict["Mail"] = a_tag[0].text
        for j in a_tag:
            if "." in j.text:
                data_dict["Website"] = j.text
        for br in i.find_all("br"):
            nextsibling = br.nextSibling
            if nextsibling and "Phone" in nextsibling:
                sibling_split = nextsibling.split(";")
                data_dict["Phone"] = sibling_split[0]
                if len(sibling_split) > 1:
                    data_dict["Fax"] = sibling_split[1]
                else:
                    data_dict["Fax"] = "There is no Fax"
        master_list.append(data_dict)
#        print(f"Mail: {mail} | Website: {website} | {phone} | {tax}")

"""
for i in chapters:
    data_dict = {}
    nextsibling = a_tag = None
    website = False
    tax = "There is no fax"
    a_tag = i.find_all("a")
    if len(a_tag) > 1 and "@" in a_tag[0].text:
        mail = a_tag[0].text
        for j in a_tag:
            if "." in j.text:
                website = j.text
        for br in i.find_all("br"):
            nextsibling = br.nextSibling
            if nextsibling and "Phone" in nextsibling:
                sibling_split = nextsibling.split(";")
                phone = sibling_split[0]
                if len(sibling_split) > 1:
                    tax = sibling_split[1]
                else:
                    tax = "There is no Fax"
        master_list.append(data_dict)
        print(f"Mail: {mail} | Website: {website} | {phone} | {tax}")
"""


excel = pd.DataFrame(master_list)
excel.to_csv("Excel.csv", index=False)
print("OK")