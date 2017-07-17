import os

from defaults import *

DEBUG = False

DATABASES['default']['NAME'] = os.path.join(PROJECT_ROOT, "dev.db")
ALLOWED_HOSTS = ['*']
SITE_ID = int(os.environ.get("SITE_ID", 2))

SECRET_KEY = "2-eu!)r7_v1unmg1s!y+1^86x!m9k#r$5fv@4yoys^t_^z2r1)"

TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgiref.inmemory.ChannelLayer",
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "prefix": u"staging",
        },
        "ROUTING": "fotaportal.routing.channel_routing",
    },
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
