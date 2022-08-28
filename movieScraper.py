from tabnanny import check
from bs4 import BeautifulSoup
from pip._vendor import requests
import re
import mysql.connector

# different movies for testing

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


#url setup
baseURL = "https://www.themoviedb.org/movie/"

movieNum = str(550)

#getting header
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:78.0) Gecko/20100101 Firefox/78.0'}







#starting number
startNum=4000

while(startNum<5000):

    # url = baseURL + movieNum
    url = baseURL + str(startNum)



    #parsing doc for general info
    result = requests.get(url, headers=headers)

    doc = BeautifulSoup(result.text, "html.parser")

    generalInfo = doc.find_all("div", {"class": "title"})

    if len(generalInfo) != 0:
        

        title = generalInfo[0].find('a').string
        date = generalInfo[0].find_all("span", {"class" : "release_date"})


        if("Collection" in title):
            print("in a collection, not valid movie")
        
        elif(len(date) == 0):
            print("does not include a date")
        else:
            date = date[0].string
            # gets info for the vote count 
            voteURLBase = "https://www.themoviedb.org/movie/"+str(startNum)+"/remote/rating/details?translate=false&language=en-US&locale=en-US"
            voteResult = requests.get(voteURLBase, headers=headers)
            doc = BeautifulSoup(voteResult.text, "html.parser")
            rating = int(doc.find_all("div", {"class":"section"})[0].find("h3").string.split(" ")[0].replace(",", ""))

            #gets the id
            id = re.split("-|>|\"", str(generalInfo[0].find_all(href=True)[0]).split('/')[2])[0]

            # tests rating
            if(rating > 2000):
                # #gets the title and adds date in case of repeat
                # if title in open('suggestions.txt').read():
                #     finalTitle = title + date

                # # gets the title
                # else :
                #     finalTitle = title
                
                # #gets the id
                # id = re.split("-|>|\"", str(generalInfo[0].find_all(href=True)[0]).split('/')[2])[0]
                

                # # prints to test
                # print(finalTitle)
                # print(id)


                # #writes to the file
                # #------------------------------------------------------
                # file_object = open('suggestions.txt', 'a')
                # # Append 'hello' at the end of file
                # file_object.write("\n\""+finalTitle+","+id+"\",")
                # # Close the file
                # file_object.close()


                # title = title.replace("\'", "\'\'")

                #inserts into sql db
                #------------------------------------------------------
                db = mysql.connector.connect(
                    # host = "localhost",
                    # user = "root",
                    # passwd = "password",
                    # database = "reegleGame"
                    host = "reegle-database.caxpaw8r0608.us-west-1.rds.amazonaws.com",
                    port = '3306',
                    database='sys',
                    user = "admin",
                    passwd = 'password'
                )

                mycursor = db.cursor()

                checkIfSameName = str("Select title from search where title=\""+title+"\"" )

                mycursor.execute(checkIfSameName)
                myresult = mycursor.fetchall()

                if(len(myresult) > 0):
                    finalTitle = str(title+date)
                else:
                    finalTitle = str(title)

                sql = "INSERT INTO search VALUES (%s, %s)"
                val = (id, finalTitle)
                mycursor.execute(sql, val)

                db.commit()
                print("movie added to db: "+finalTitle +" id: "+ str(id))

            else:
                print("movie does not have enough votes: ", title+" id: "+ str(id))
                if(rating > 1000):
                    #writes to the file
                    #------------------------------------------------------
                    file_object = open('almostMovies.txt', 'a')
                    # Append 'hello' at the end of file
                    file_object.write(str("\n\""+title+","+str(id)+"\","))
                    # Close the file
                    file_object.close()

    else:
        print("not a movie in existance id: "+ str(id))

    startNum+=1
    # print(x)
