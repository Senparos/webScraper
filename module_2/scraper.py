#this file deals with retrieving the information from websites, and cleaning the data. this is done with the requests and beautifulsoup packages
#this file implements the single responsibility principle by havin gone function that deals with the single task of scraping the data

import requests
from bs4 import BeautifulSoup

def getProcData(url):
    html = requests.get(url)
    data = BeautifulSoup(html.content, "lxml")
    text = ""
    for body in data.find_all("p"):
        text += body.text
    return text
