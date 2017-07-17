# TODO: can we move this to livedevice app?
from channels.routing import route

from livedevice.consumers import (
    ws_connect,
    ws_disconnect,
    gis_locate,
    mbedcloudaccount_connect,
    mbedcloudaccount_poll,
)

channel_routing = [
    route("websocket.connect", ws_connect),
    route("websocket.disconnect", ws_disconnect),
    route("gis.locate", gis_locate),
    route("mbedcloudaccount.connect", mbedcloudaccount_connect),
    route("mbedcloudaccount.poll", mbedcloudaccount_poll),
]
