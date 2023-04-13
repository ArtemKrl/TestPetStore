import requests
from utils.config import Config


class BasePage:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.url = Config.base_url + endpoint
        self.response = None

    def send_request(self, method, **kwargs):
        self.response = requests.request(method, self.url, **kwargs)
        return self.response