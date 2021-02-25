from django.apps import AppConfig


class CatAppConfig(AppConfig):
    name = 'cat_app'

    def ready(self):
        import cat_app.signals
        
