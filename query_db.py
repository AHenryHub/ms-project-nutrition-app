from flask import Flask,jsonify
from pysondb import db

"""
Adding to db

a=db.getDb("pathtojson.json")
>> a.add({"name":"pysondb","type":"DB"})
>> # returns 1929323232 which is a ID assigned to the above data.
>> a.add({"namme":"pyson","type":"DB"})
"""

"""
Query db

a=db.getDb("path.json")
>> a.getBy({"type":"CLI"})
>> [{"name":"py_cli","type":"CLI"},{"name":"py_cli2","type":"CLI"}]
>> a.getBy({"name":"py_cli"})
>> [{"name":"py_cli","type":"CLI"}]
"""


def query():
    base = db.getDb("db.json")
    base.add({"name":"recipebook","type":"DB"})

    print(base.getBy({"type":"DB"}))

    return base

query()