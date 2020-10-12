import redis
import json

r = redis.StrictRedis()
reply = json.loads(r.execute_command('JSON.MGET','89b2c519c47ffff'))
print (reply)
