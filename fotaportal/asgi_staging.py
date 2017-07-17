import os
from channels.asgi import get_channel_layer

os.environ["DJANGO_SETTINGS_MODULE"] = "fotaportal.settings.staging"

channel_layer = get_channel_layer()
