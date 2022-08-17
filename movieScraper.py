from bs4 import BeautifulSoup
from pip._vendor import requests

url = "https://www.themoviedb.org/movie/696806"
# url = "https://www.themoviedb.org/movie/1"

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'}

result = requests.get(url, headers=headers)

doc = BeautifulSoup(result.text, "html.parser")

mydivs = doc.find_all("div", {"class": "single_column"})

tag = doc.body

print(mydivs)