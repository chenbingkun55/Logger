import os
import sys

sys.path.append('lib')
import bigquery as db
_db = None

def init():
    _db = db.create_engine()



init()
