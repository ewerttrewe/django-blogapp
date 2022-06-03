from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        import users.signals
        # Explicitly connect a signal handler.
        