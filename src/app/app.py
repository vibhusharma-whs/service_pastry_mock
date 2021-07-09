#!/usr/bin/env python3
import connexion
import logging
import json

from connexion import NoContent

def write_to_file(content):
    with open("./mock_pastries.json", "w") as pastries:
        pastries.write(json.dumps(content))


def read_from_file():
    with open("./mock_pastries.json", "r") as pastries:
        return json.loads(pastries.read())

def get_pastries():
    pastries = read_from_file()
    result = []
    for k, v in pastries.items():
        current_pastry = {"name": k, **v}
        result.append(current_pastry)

    return result


logging.basicConfig(level=logging.INFO)
app = connexion.App(__name__)
app.add_api('pastry_api.yaml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :5000 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=5000, server='gevent')