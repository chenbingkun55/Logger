import os
import sys

sys.path.append('lib')
import bigquery as db

def init():
    return db.create_engine()



_db = init()
