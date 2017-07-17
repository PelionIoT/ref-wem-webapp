from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.views.generic import RedirectView

from django.contrib import admin

urlpatterns = [
    url(r"^$", RedirectView.as_view(url=reverse_lazy('livedevice'), permanent=False), name="home"),
    url(r"^live-device/", include("livedevice.urls")),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
