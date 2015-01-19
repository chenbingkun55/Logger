import easybigquery as bqapi

projectNumber = '790642131213'
serviceEmail = '790642131213-fnqf4v6r3useipq1595cm8qicmbe71vd@developer.gserviceaccount.com'
pathToKeyfile = 'key.pem'

API = bqapi.GoogleAPIFromServiceAccount(projectNumber, serviceEmail, pathToKeyfile)
bq = bqapi.GoogleBigQuery(API)

def rawNgramData(word):
    query = "SELECT ngram, cell.volume_fraction FROM publicdata:samples.trigrams WHERE ngram CONTAINS '%s' GROUP BY ngram, cell.volume_fraction;" % word
    return bq.query(query)

print rawNgramData("robot")
