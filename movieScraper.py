from bs4 import BeautifulSoup
from pip._vendor import requests

#adam project 16
# url = "https://www.themoviedb.org/movie/696806" 

#top gun maverick 17
# url = "https://www.themoviedb.org/movie/361743"

#sorcerers 29
url = "https://www.themoviedb.org/movie/27022-the-sorcerer-s-apprentice"

#first movie in db
# url = "https://www.themoviedb.org/movie/1"

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'}

result = requests.get(url, headers=headers)

doc = BeautifulSoup(result.text, "html.parser")

mydivs = doc.find_all("div", {"class": "single_column"})

generalInfo = doc.find_all("div", {"class": "ott_true"})

# tag = doc.body

# print(mydivs)

print(generalInfo)