#author: Jay Sanders
#due: 2024-02-13
#class: CS 325

import requests
from bs4 import BeautifulSoup

def main() -> None:
    # session = HTMLSession()
    file = open("input.txt", "r")
    url = file.readline().strip()
    counter = 1
    while url:
        html = requests.get(url)
        data = BeautifulSoup(html.content, "lxml")
        text = ""
        for body in data.find_all("p"):
            text += body.text
        output = open(f"output{counter}.txt", "w")
        output.write(text)
        output.close()
        counter += 1
        url = file.readline().strip()
    file.close()
    
if __name__ == "__main__":
    main()