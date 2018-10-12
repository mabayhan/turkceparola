#!/usr/bin/env python3.6
from flask import Flask,jsonify,make_response

import sqlite3,sys,random
# import sys
# import random


conn = sqlite3.connect('list.db')
c = conn.cursor()


 
l0 = "çÇğĞıİöÖşŞüÜâÂîÎûÛ"
l1 = "ccggiioossuuaaiiuu"
l2 = str.maketrans(l0, l1)

k0 = "abcdefghiikoqsstvvxy"
k1 = "@8(63#9#1!<095$+><%?"
k2 = str.maketrans(k0, k1)


# f = open("myfile.txt", "w")
r0 = random.randrange(2,8)
# r1 = 7 - r0
r1 = random.randrange(2,8)

r3 = random.randrange(0,999)
# a = '!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','`','{','¦','}','~','\\'
a = '!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','{','¦','}','~','\\'
b = '0','1','2','3','4','5','6','7','8','9'

# c.execute('SELECT * FROM wordlist where word_len = ? ORDER BY RANDOM() LIMIT 1;' , (r,))
# row = c.fetchone()
# if row != None:
#     row = c.fetchone()
# else:
#     print("else")

# for i in range(2,8):
def wo(r,t = ''):
    c.execute('SELECT * FROM wordlist where word_len = ? LIMIT 1;' , (r,))
    row = c.fetchone()
    
    if (row != None):
        # t2 = row[0]
        t1 = row[1].translate(l2).lower().capitalize()
        if(t):
            t1 = list(t1)
            r = random.randrange(1,len(t1))
            
            t1[r] = t1[r].translate(k2)
            t1 = "".join(t1)
            # print(t1)
        t0 = row[1].lower().capitalize()
    else:
        t0 = ''
        t1 = ''
    return [t0,t1]

x1 = wo(r0)
y1 = wo(r1,1)
z1 = str(r3)
t1 = random.choice(a)

results = [
    {
        'id': 0,
        'fw': x1[0],
        'sw': y1[0],
        'lw': x1[1]+t1+y1[1]+str(r3)
    }
]

# for i in range(1,6):


#     x1 = wo(r0)
#     y1 = wo(r1,1)
#     z1 = str(r3)
#     t1 = random.choice(a)

#     # print("\n" + x1[0]+' '+y1[0] + '\n' + x1[1]+t1+y1[1]+str(r3) + "\n")

#     results = [
#         {
#             'id': i,
#             'fw': x1[0],
#             'sw': y1[0],
#             'lw': x1[1]+t1+y1[1]+str(r3)
#         }
#     ]

#     i = i+1

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/random/1', methods=['GET'])
def get_task():
    return jsonify({'task': results[0]})

if __name__ == '__main__':
    app.run(debug=True)