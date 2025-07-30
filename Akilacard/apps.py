from django.apps import AppConfig

class ProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Akilacard'

    def ready(self):
        import Akilacard.signals  # Ensures signals are connected when the app is ready
