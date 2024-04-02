# Simple Python Web Scraper v2.0

## Description

This program is designed to scrape news articles from news websites. It has been tested with NPR, CNN, and Fox News. It uses the "BeautifulSoup" and "requests" libraries in Python to scrape and clean this data, as well as the "OpenAI" package to create a summary of each article

## Requirements

To run this program, you must have the following:\
    - GIT, newest version\
    - Miniconda, a minimal installer for conda. After importing the yml file you will have the following packages(among others)\
        - Python 3.12\
        - BeatifulSoup4 python package 4.12\
        - requests python package 2.31\
        - OpenAI python package 1.14\
        - OpenAI account with api credits\
        - OpenAI API key\

## Installation

    1. download "requirements.yml" file from the following GitHub repository: (https://github.com/Senparos/webScraper)\
    2. launch Miniconda and use the following command to create a new environment:  conda env create -f requirements.yml\
    3. activate this environment with the following command: conda activate requirements\
    4. verify that the packages that are required are listed when you enter the following command into the prompt: conda list\

## Creating an OpenAI account and obtaining an API key

    1. 


## Using the program

    1. create a file named "input.txt" and put any number of urls that lead to news articles(as mentioned above, this has been tested with NPR, CNN, and Fox News), keeping links on their own lines\
    2. launch Anaconda Prompt(Miniconda3)\
    3. use the following command to activate the environment needed to run this program: conda activate requirements\
    4. run the program by typing the following into the Anaconda prompt: python scraper.py\
    5. during execution, the program will create an output for each news article, which is named output#.txt, where the # represents which link it corresponds to\
    6. 
