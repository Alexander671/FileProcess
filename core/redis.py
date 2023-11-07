import redis

from .settings import REDIS_URL

conn = redis.Redis.from_url(REDIS_URL)
