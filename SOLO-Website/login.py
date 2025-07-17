import sqlite3 
import hashlib

conn = sqlite3.connect('userdata.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS userdata(
           Id INTEGER PRIMARY KEY,
           username VARCHAR(255) NOT NULL,
           password VARCHAR(255) NOT NULL
           )""")

username1, password1 = "icesceam", hashlib.sha256("vanillaicecream".encode()).hexdigest()
username2, password2 = "sphagetti", hashlib.sha256("sphagettiandmeatballs".encode()).hexdigest()
username3, password3 = "bread", hashlib.sha256("garlicbread".encode()).hexdigest()
username4, password4 = "pizza", hashlib.sha256("cheesepizza".encode()).hexdigest()
username5, password5 = "burger", hashlib.sha256("hamburger".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username5, password5))


conn.commit()