# Simple Python Web Scraper v2.0.1

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
        - OpenAI API key

## Installation

    1. download "requirements.yml" file from the following GitHub repository: (https://github.com/Senparos/webScraper)\
    2. launch Miniconda and use the following command to create a new environment:  conda env create -f requirements.yml\
    3. activate this environment with the following command: conda activate requirements\
    4. verify that the packages that are required are listed when you enter the following command into the prompt: conda list

## Creating an OpenAI account and obtaining an API key

    1. navigate to openai.com\
    2. select "log in" in the upper right\
    3. select "sign up"\
    4. enter your email address and select "continue"
    5. enter a password and select "continue"
    6. verify your email address by following the link sent to your email 
    7. once logged in, select "API" from the home screen
    8. select "API keys" from the navigation menu on the left side of the screen
    9. select "create new secret key"
    10. name the key using the box provided and select "Create secret key"
    11. open the file "apiKey.txt" found in the root of the project and replace the "KEY_PLACEHOLDER" with your API key


## Using the program

    1. create a file named "input.txt" and put any number of urls that lead to news articles(as mentioned above, this has been tested with NPR, CNN, and Fox News), keeping links on their own lines\
    2. launch Anaconda Prompt(Miniconda3)\
    3. use the following command to activate the environment needed to run this program: conda activate requirements\
    4. run the program by typing the following into the Anaconda prompt: python scraper.py\
    5. during execution, the program will create an output for each news article, which is named output#.txt, where the # represents which link it corresponds to\
    6. the program will also generate a summary of each article, which can be found in the \Data\summary folder and will be named summary#.txt, where # represents which link the summary corresponds to
