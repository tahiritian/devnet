import json

jsonstr = """{"people":[{"Id":"1","FirstName":"Benjamin","LastName":"Finkel",
    "Email":"ben.finkel@cbtnuggets.com"},{"Id":"2","FirstName":"Jane","LastName":"Doe",
    "Email":"jane.doe@cbtnuggets.com"},{"Id":"3","FirstName":"Pat","LastName":"Smith",
    "Email":"pat.smith@cbtnuggets.com"}]}"""

jsonobj = json.loads(jsonstr)

print(jsonobj['people'][1])

jsonobj = json.load(open('sample.json'))

print(jsonobj['people'])