"""URLs for live-device
"""
from django.conf.urls import url
from django.conf import settings

from livedevice.views import (
    device_finder,
    livedevice,
    mbed_cloud_webhook,
    showcache,
)

urlpatterns = [
    url(r"^$", livedevice, name="livedevice"),
    url(r"^find/$", device_finder, name="find"),
    url(r"^mbed-cloud-webhook/$", mbed_cloud_webhook, name="mbed cloud webhook"),
]

if settings.DEBUG:
    urlpatterns.append(url(r"^cache/$", showcache, name="show cache"))
