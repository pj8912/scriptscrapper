import requests
from bs4 import BeautifulSoup

url = input("URL:")
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")
pre_text = soup.find("pre").get_text()

print(pre_text)
