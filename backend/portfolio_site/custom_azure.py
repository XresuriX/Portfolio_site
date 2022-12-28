from storages.backends.azure_storage import AzureStorage
import environ
from django.conf import settings

env = environ.Env()
environ.Env.read_env()


class AzureMediaStorage(AzureStorage):
    account_name = env("azure_account_name")
    account_key = env('azure_account_key')
    azure_container = "media"
    expiration_secs = None
    overwrite_files = False


class AzureStaticStorage(AzureStorage):
    account_name = env("azure_account_name")
    account_key = env('azure_account_key')
    azure_container = "static"
    expiration_secs = None
    overwrite_files = False
