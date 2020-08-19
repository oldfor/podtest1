#_*_encoding='utf-8'_*_

'''
author:@chengxm
time:2020/8/19 16:03
'''
import sqlite3

conn = sqlite3.connect('test.db')
print ("Opened database successfully")
c = conn.cursor() # 获取当前游标
# c.execute('''CREATE TABLE COMPANY
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
# print ("Table created successfully")

c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")

conn.commit()
conn.close()