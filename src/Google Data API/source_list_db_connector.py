'''
Created on 15-Jun-2016

@author: rushabh.a.sheth


Added sample channel ids to mysql db
Connected to mysql db using pyton and printed the channel ids
'''
#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="rushabh@",  # your password
                     db="jarvisschema")  #  name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM source_list")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[2] 

db.close()