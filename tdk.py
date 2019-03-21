#!/usr/bin/env python3.6
import requests
import sqlite3
import string
from bs4 import BeautifulSoup
from urllib import parse

from collections import defaultdict

import requests
import urllib.parse


conn = sqlite3.connect('list.db')
c = conn.cursor()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# r = '3'

def fetch(url, data=None):
    if data is None:
        return s.get(url).content
    else:
        return s.post(url, data=data).content

for r in range(4,13):
    print("counter number :{}".format(r))
    # c.execute('select * from wordlist where word_len = ?; ', (r,))
    c.execute('select * from wordlist where word_desc is NULL and word_desc_exist is not 0;')

    rows = c.fetchall()
    for row in rows:

        URL = 'http://tdk.gov.tr/index.php?option=com_gts&arama=gts&guid=TDK.GTS.5b8f0facbe41f8.01703955'
        s = requests.Session()

        soup = BeautifulSoup(fetch(URL), "html.parser")
        form = soup.find('form')
        fields = form.findAll('input')

        formdata = {'kelime' : 'kelime'}

        print("loop word : {cs} {m} {ce}".format(m = row[1],cs = bcolors.OKBLUE, ce = bcolors.ENDC))

        # formdata['kelime'] = 'SÜRŞARJ'
        formdata['kelime'] = row[1]

        # print(formdata)
        posturl = parse.urljoin(URL, form['action'])
        # print(posturl)
        try:
            r = s.post(posturl, data=formdata)
            s = BeautifulSoup(r.text, "html.parser")
        except Exception as e:
            print(e)    
            pass
        try:
            t = s.find('table', {"id": "hor-minimalist-a"})

            t = t.find_all('td')
            # print("\n\n=================================\n\n")
            # for i in t:
            #     tx1 = "".join([str(x) for x in i.contents]).replace('<br/>','').strip()
            #     # print(tx1)
            #     print(row[1].strip() + " : " + tx1)       
                
            tx1 = "".join([str(x) for x in t[0].contents]).replace('<br/>','').replace('1.','').replace('index.php','http://tdk.gov.tr/index.php').strip()  
            #print(row)
            c.execute("UPDATE wordlist Set word_desc = ? where word_id = (select word_id from wordlist where word_text = ? limit 1)", (tx1,row[1],))
            print("loop word meaning : {cs} {m} {ce}".format(m = tx1, cs = bcolors.WARNING, ce = bcolors.ENDC))
            conn.commit()
        except Exception as e: 
            # print(e)
            c.execute("UPDATE wordlist Set word_desc_exist = 0 where word_id = ?", (row[0],))
            conn.commit()
            # print("error with " + str(row[1]))
            print("error with ")
            pass 
