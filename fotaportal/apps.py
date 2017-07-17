from importlib import import_module

from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):

    name = "fotaportal"

    def ready(self):
        import_module("fotaportal.receivers")
