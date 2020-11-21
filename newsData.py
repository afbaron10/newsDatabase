import sqlite3
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import csv, xlsxwriter

conn = sqlite3.connect(r'C:\Users\andre\Downloads\OneDrive_2020-06-17\Catalina-Asistente virtual\intento1\bin\Debug\popo.sqlite')
cur = conn.cursor()


cur.execute('''delete from NEWS''')


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.eltiempo.com/"
html = urllib.request.urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, 'html.parser')

lst = list()
# Recuperar todas las etiquetas de anclaje
for article in sopa.find_all("h3", class_="listing-title box-title"):
    ##headline = article.h3.a
    ##print(headline.text)
    headline = (article.text)
    lst.append(headline)


for item in lst:
    cur.execute('''INSERT INTO NEWS (noticia)
                VALUES (?)''', (item,))
    conn.commit()
cur.close()
