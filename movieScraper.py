from bs4 import BeautifulSoup
from pip._vendor import requests
import mysql.connector


baseURL = "https://www.themoviedb.org/movie/"

movieNum = str(550)

url = baseURL + movieNum

#fight club
# url = "https://www.themoviedb.org/movie/550"

#adam project 16
# url = "https://www.themoviedb.org/movie/696806" 

#top gun maverick 17
# url = "https://www.themoviedb.org/movie/361743"

#sorcerers 29
# url = "https://www.themoviedb.org/movie/27022-the-sorcerer-s-apprentice"

#first movie in db
# url = "https://www.themoviedb.org/movie/1"

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36'}

result = requests.get(url, headers=headers)

doc = BeautifulSoup(result.text, "html.parser")

# print(doc)

generalInfo = doc.find_all("div", {"class": "title"})


voteURLBase = "https://www.themoviedb.org/movie/"+movieNum+"/remote/rating/details?translate=false&language=en-US&locale=en-US"

voteResult = requests.get(voteURLBase, headers=headers)

doc = BeautifulSoup(voteResult.text, "html.parser")

rating = doc.find_all("div", {"class":"section"})[0].find("h3").string.split(" ")[0]

print(rating)

# voteCount = str(doc.find_all("script")[12])

# print(voteCount)

if len(generalInfo) != 0:
    title = generalInfo[0].find('a').string

    id = str(generalInfo[0].find_all(href=True)[0]).split('/')[2].split('-')[0]

    date = generalInfo[0].find_all("span", {"class" : "release_date"})[0].string

    print(title)
    print(id)
    print(date)


    # db = mysql.connector.connect(
    #     host = "localhost",
    #     user = "root",
    #     passwd = "password",
    #     database = "reegleGame"
    # )

    # mycursor = db.cursor()

    # sql = "INSERT INTO search VALUES (%s, %s)"
    # val = (550, "Fight Club")
    # mycursor.execute(sql, val)

    # db.commit()






# print(mydivs)

# print(generalInfo)