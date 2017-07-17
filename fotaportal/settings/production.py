import os

from defaults import *

DEBUG = False

DATABASES['default']['NAME'] = os.path.join(PROJECT_ROOT, "dev.db")
ALLOWED_HOSTS = ['*']
SITE_ID = int(os.environ.get("SITE_ID", 2))

TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "prefix": u"production",
        },
        "ROUTING": "fotaportal.routing.channel_routing",
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
