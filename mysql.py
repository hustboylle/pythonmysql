# _*_ coding: utf-8 _*_
import  pymysql
import requests
from random import randint
from selenium import webdriver


db =pymysql.connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="*******",
    db="tibetwebsite")
cursor=db.cursor()
sql="select * from tibetwebsite where id>10 and id<15"

try:
    cursor.execute(sql)
    results=cursor.fetchall()
    print(results)

    for row in results:
        id=row[0]
        webname=row[1]
        url=row[2]
        print(url)
        try:
            r = requests.get(url, allow_redirects=False)
            if r.status_code==200:
                print(url,r.status_code)
            else:
                print(url, r.status_code)
        except Exception as e:
            print(e)
except:
    print("Error: unable to fetch data")

db.close()
