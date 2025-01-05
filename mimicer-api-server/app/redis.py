import redis
import env

redis_client = None

def get_redis_client():
    global redis_client
    if redis_client is None:
        pool = redis.ConnectionPool(host=env.REDIS_HOST, port=env.REDIS_PORT, db=0)
        redis_client = redis.StrictRedis(connection_pool=pool)
    return redis_client