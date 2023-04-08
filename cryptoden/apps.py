from django.apps import AppConfig


class CryptodenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cryptoden'

    def ready(self):
        import cryptoden.signals