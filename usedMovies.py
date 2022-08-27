from tabnanny import check
from bs4 import BeautifulSoup
from pip._vendor import requests
import re
import mysql.connector



f = open("movies.txt", "r")
for x in f:
    seperated = x.rsplit(',',2)
    title = seperated[0].replace('\"',"")
    id = seperated[1].replace('\"',"")
    print(title)
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

    sql = "INSERT INTO search VALUES (%s, %s)"
    val = (id, title)
    mycursor.execute(sql, val)

    db.commit()