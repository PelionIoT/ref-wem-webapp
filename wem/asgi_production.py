import os
from channels.asgi import get_channel_layer

os.environ["DJANGO_SETTINGS_MODULE"] = "wem.settings.production"

channel_layer = get_channel_layer()
