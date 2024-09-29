# myproject/__init__.py
from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ("celery_app",)


import redis

REDIS_HOST = "redis"  # or your Redis server's address
REDIS_PORT = 6379  # or your Redis server's port
REDIS_DB = 0  # or your Redis database number

# Create a Redis connection
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)
