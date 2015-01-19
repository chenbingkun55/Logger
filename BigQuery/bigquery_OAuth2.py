#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#
#

"""
Usage:
  $ python tasks.py
"""

__author__ = 'chenbingkun55@163.com (ChenBK)'

import httplib2
import pprint
import sys

from googleapiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

key_file = 'key.p12'
client_mail = '790642131213-fnqf4v6r3useipq1595cm8qicmbe71vd@developer.gserviceaccount.com'
scope = 'https://www.googleapis.com/auth/bigquery'
projectId='nth-honor-819'
datasetId='Temp'
tableId='Account'


def main(argv):
  # Load the key in PKCS 12 format that you downloaded from the Google API
  # Console when you created your Service account.
  f = file(key_file, 'rb')
  key = f.read()
  f.close()

  # Create an httplib2.Http object to handle our HTTP requests and authorize it
  # with the Credentials. Note that the first parameter, service_account_name,
  # is the Email address created for the Service account. It must be the email
  # address associated with the key that was created.
  credentials = SignedJwtAssertionCredentials(client_mail,key,scope)

  http_auth = credentials.authorize(httplib2.Http())

  service = build("bigquery", "v2", http=http_auth)

  # List all the tasklists for the account.
  response = service.tables().get(projectId=projectId,datasetId=datasetId,tableId=tableId).execute()
  #lists = service.tasklists().list().execute(http=http)
  #pprint.pprint(lists)
  pprint.pprint(response)


if __name__ == '__main__':
  main(sys.argv)
