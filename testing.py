import sqlite3
from os import getenv
from shutil import copyfile
import pywintypes
import win32crypt
import os


print(getenv('APPDATA'))