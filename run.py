#author: Jay Sanders
#this file utilizes both module_1 and module_2 to scrape news articles
#input goes in the \Data\raw\raw.txt file, with each url on a separate line
#this python file uses the Open-Closed Principle by allowing users to add functionality to the scraper by adding in more modules instead of having everything in one file

from module_1 import file
from module_2 import scraper
import os

def main():
    cwd = os.getcwd()
    path1 = "Data"
    path2 = "raw"
    path3 = "raw.txt"

    fileObj = file.op(os.path.join(cwd, path1, path2, path3), "r")
    url = file.read(fileObj)
    counter = 1
    while url:
        file.wr(scraper.getProcData(url), counter)
        url = file.read(fileObj)
        counter += 1
if __name__ == "__main__":
    main()