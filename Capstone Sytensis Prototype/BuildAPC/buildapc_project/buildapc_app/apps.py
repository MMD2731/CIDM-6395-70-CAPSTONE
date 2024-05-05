# buildapc_app/apps.py
from django.apps import AppConfig

class BuildapcAppConfig(AppConfig):
    name = 'buildapc_app'

    def ready(self):
        from .utils import create_user_groups
        create_user_groups()  # Call function to create user groups
