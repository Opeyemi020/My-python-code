import json

record = {"student_records": [
    {"id": 1, "name": "ebuka", "age": 41},
    {"id": 2, "name": "dele", "age": 44},
    {"id": 3, "name": "sultan", "age": 31},

]}

with open("record.json", mode='w') as rec:
    json.dump(record, rec)

with open("record.json", mode='r') as rec2:
    print(json.dumps(json.load(rec2), indent=4))


