#!/usr/bin/env python3.6
import requests
import sqlite3
import string
from bs4 import BeautifulSoup



# print(soup.prettify())
# print(list(soup.children))

conn = sqlite3.connect('list.db')
c = conn.cursor()
d = 'abcçdefgğhıijklmnoöprsştuüvyz'

#prevent accidantly execution
rs = 0

if ( rs == 1 ):
    for m in d:
        for j in range(3,13):
            u = "https://kelimeler.net/"+str(m)+"-ile-baslayan-"+ str(j) +"-harfli-kelimeler"
            page = requests.get(u)
            soup = BeautifulSoup(page.content, 'html.parser')
            t = soup.find_all('a', class_='ListedWordLink mobile-link')
            for i in t:
                # print(i.get_text())
                c.execute("INSERT INTO wordlist(word_len,word_text) values (?,?)", (j,i.get_text().strip(),))
                conn.commit()
            print(u)

# for m in 'abcçdefgğhıijklmnoöprsştuüvyz':
#     for j in [3,4,5,6,7,8,9]:
#         print (str(m) + ' ' + str(j))

# Save (commit) the changes

# for row in c.execute('SELECT * FROM wordlist'):
#     print(row)

#print(t)
