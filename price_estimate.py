import random
from flask import Flask
import query_db


def prices():
    cost = random.randrange(100,1000,1) / 100.0
    return("$" + str(cost))

#prices()