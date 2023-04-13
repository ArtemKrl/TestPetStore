from pages.base_page import BasePage


class PostPetPage(BasePage):
    def __init__(self, json):
        super().__init__("/pet")
        self.json = json

    def send_request(self, **kwargs):
        self.response = super().send_request("POST", json=self.json, **kwargs)
        return self.response