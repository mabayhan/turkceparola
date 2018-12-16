#!/usr/bin/env python3
import sqlite3
import sys
import random
import sys

conn = sqlite3.connect('list.db')
c = conn.cursor()

l0 = "çÇğĞıİöÖşŞüÜâÂîÎûÛ"
l1 = "ccggiioossuuaaiiuu"
l2 = str.maketrans(l0, l1)

k0 = "abcdefghiikoqsstvvxy"
k1 = "@8(63#9#1!<095$+><%?"
k2 = str.maketrans(k0, k1)

into_a = 13

try:
    into_a = int(sys.argv[1]) + 1
    pass
except:
    # print("Default 12 char password")
    pass

# if(len(sys.argv) > 0):
#     into_a = int(sys.argv[1]) + 1
#     # print(into_a)
# else:
#     into_a = 13




r0 = random.randrange(3,into_a)
r1 = into_a - r0 - 1

# r0 = random.randrange(3,13)
# r1 = 12 - r0



a = '!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<','=','>','?','@','[',']','^','_','{','¦','}','~','\\'
b = '0','1','2','3','4','5','6','7','8','9'

def wo(r,t = '',stype=0):
    c.execute('SELECT * FROM wordlist where word_len = ? ORDER BY RANDOM() LIMIT 1;' , (r,))
    # if(stype == 0):
    #     c.execute('SELECT * FROM wordlist where word_len = ? and word_desc like \'%<i>s%fat</i>%\' ORDER BY RANDOM() LIMIT 1;' , (r,))
    # else:
    #     c.execute('SELECT * FROM wordlist where word_len = ? ORDER BY RANDOM() LIMIT 1;' , (r,))

    row = c.fetchone()
    
    if (row != None):
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

x1 = wo(r0,1)
y1 = wo(r1,1)
r3 = random.randrange(0,999)
z1 = str(r3)
t1 = random.choice(a)


# print("Enter a password length between (4 and 12)")

# print("strings x1: {}, y1: {}, z1: {}, t1: {}, r0: {}, r1: {}".format(x1,y1,z1,t1,r0,r1))

# i = 0 
# j = ''

# while(i < (len(x1[0]) + len(y1[0]))):
#     i = i+1

# # print(i)
# # print("j: " + j + ":")
# k = 0 
# while(k < 20 - i):
#     j = ' ' + j
#     k = k + 1

# if(len(y1[0]) < 1 | len(x1[0]) < 1 ):
#     spacer = j +  ' :: \t'
# else:
#     spacer = j +  '  :: \t'

spacer = '\t :: \t'    

print(x1[0]+' '+y1[0] + spacer + x1[1]+t1+y1[1]+z1)
# print(x1[1]+t1+y1[1]+z1)

conn.close()