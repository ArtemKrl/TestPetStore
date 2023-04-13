from pages.base_page import BasePage


class GetPetPage(BasePage):
    def __init__(self, pet_id):
        super().__init__(f"/pet/{pet_id}")