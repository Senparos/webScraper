from xml.etree import ElementTree as ET
import os

# IMPORTANT: Must update NUM_ARTICLES constant with the correct number of articles to work
NUM_ARTICLES = 10

def txt_to_html(txt_file, html_file):
  """
  Converts a text file with header and paragraph to an HTML file.
  Make necessary changes for multiple news articles. This script is
  only for one news article.

  Args:
      txt_file (str): Path to the text file.
      html_file (str): Path to the output HTML file.
  """
  # Read text file content
  with open(txt_file, 'r') as f:
    content = f.readlines()


  #TESTING CODE
  # for i in range(len(content)):
  #   print(content[i])
  print(len(content))

  # Extract header and paragraph, since you will be having multiple articles the logic will
  # change for the code given below. 
  #moved to line 32

  # Create root element for HTML, try to remember the structure of a HTML file
  root = ET.Element("html")

  # Create head and body elements, try to understand how subElements works
  head = ET.SubElement(root, "head")
  title = ET.SubElement(head, "title")
  title.text = "My News Aggregation Site"
  body = ET.SubElement(root, "body")

  # Create header and paragraph elements in body
  # Placed all of the header and paragraph logic into a for loop to handle multiple articles
  for i in range(0, NUM_ARTICLES * 2, 2):
    header = content[i].strip()
    paragraph = content[i+1].strip()

    # h1 = ET.SubElement(body, "h1")
    # h1.text = header
    ET.SubElement(body, "h1").text = header
    ET.SubElement(body, "p").text = paragraph
    # p = ET.SubElement(body, "p")
    # p.text = paragraph

  # Write HTML tree to file
  with open(html_file, 'wb') as f:
    tree = ET.ElementTree(root)
    tree.write(f, encoding='utf-8')

def gather_data(num_articles):
  my_text = ""

  with open("my_text.txt", "w") as out_file:
    for i in range(num_articles):
      with open(os.path.join("..", "Data", "summary", f"summary{i + 1}.txt"), "r") as file:
        title = file.readline().strip()
        body = file.readline().strip()
        #  my_text += title
        #  my_text += body
        out_file.write(f"{title}\n{body}\n")
  
  # out_file.write(my_text)


txt_file = "my_text.txt"
html_file = "all_news_articles.html"
gather_data(NUM_ARTICLES)
txt_to_html(txt_file, html_file)

print(f"Converted text file '{txt_file}' to HTML file '{html_file}'.")
