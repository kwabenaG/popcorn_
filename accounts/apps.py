from django.apps import AppConfig


# accounts apps config file
class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        from . import signals  # callback function for account app
