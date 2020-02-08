from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # Import signals
    def ready(self):
        import users.signals
