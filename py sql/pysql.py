# author Alexis Folse
#python 3.10.6

import sqlite3 # imports sql so it can read the sql codes

conn = sqlite3.connect('PySQLTXT.db')


with conn:
    cur = conn.cursor()
    #the next code prevents duplicate table froming and errors being thrown
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtFiles(ID INTEGER PRIMARY KEY AUTOINCREMENT, file_name TEXT,  date_modified TEXT)")
    conn.commit()

# list 
files = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# what to print 
for x in files:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO tbl_txtFiles (file_name) VALUES (?)', (x,))
            print(x)
conn.close()
