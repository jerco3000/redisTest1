import json
from rejson import Client, Path

rj = Client(host='localhost', port=6379, decode_responses=True)


""" obj = {
    'answer': 42,
    'arr': [None, True, 3.14],
    'truth': {
        'coord': 'out there'
    }
}
rj.jsonset('obj1', Path.rootPath(), obj) """

# temp = rj.jsonget('89b2c519c47ffff', Path('.'))
temp = rj.jsonmget(Path('.'), '89b2c519c47ffff', '89b2c519c48ffff', '89b2c519c49ffff')
print (json.dumps(temp))
