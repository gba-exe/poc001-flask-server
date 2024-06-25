
from flask import json
from multipledispatch import dispatch

@dispatch(object)
def to_json(obj):
    generated_json = json.dumps(obj, default=lambda o: o.__dict__)
    return json.loads(generated_json)

@dispatch(list)
def to_json(obj):
    for i in range(len(obj)):
        obj[i] = to_json(obj[i])

    return obj