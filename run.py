#author: Jay Sanders
#this file utilizes both module_1 and module_2 to scrape news articles
#input goes in the \Data\raw\raw.txt file, with each url on a separate line
#this python file uses the Open-Closed Principle by allowing users to add functionality to the scraper by adding in more modules instead of having everything in one file

from module_1 import file
from module_2 import scraper
import os
from openai import OpenAI

def main():
    cwd = os.getcwd()
    path1 = "Data"
    path2 = "raw"
    path3 = "raw.txt"
    
    #reading file called apiKey.txt that contains the API key from openAI
    keyFile = file.op("apiKey.txt", "r")
    key = keyFile.readline()

    #creating an OpenAI object
    client = OpenAI(api_key=key)

    #uses the os package to get the current working directory
    fileObj = file.op(os.path.join(cwd, path1, path2, path3), "r")
    url = file.read(fileObj)
    counter = 1

    #this loop uses the scraper module and the openai package
    while url:
        content = scraper.getProcData(url)
        file.wr(content, counter)
        url = file.read(fileObj)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a journalists that can write concise summaries of news articles given the text from said article."},
                {"role": "user", "content": f"Summarize the following article in no more than 50 words: {content}"}
            ]
            )
        file.wrSum(completion.choices[0].message.content, counter)
        counter += 1
        
if __name__ == "__main__":
    main()