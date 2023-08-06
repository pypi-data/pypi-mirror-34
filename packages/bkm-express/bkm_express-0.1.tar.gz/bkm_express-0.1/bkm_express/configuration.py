from client_exceptions import ConfigurationError
from utils import format_key
from settings import ENV_URLS


class Configuration(object):
    def __init__(self, environment, merchant_id, merchant_private_key):
        self.environment = environment
        self.merchant_id = merchant_id
        self.merchant_private_key = self._merchant_private_key(merchant_private_key)
        self.baseUrl = ENV_URLS.get(environment)
        if not self.baseUrl:
            raise ConfigurationError("You should set a valid environment")

    def _merchant_private_key(self, merchant_private_key):
        return format_key(merchant_private_key)
