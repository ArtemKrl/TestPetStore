
import allure
from pages.get_pet_page import GetPetPage


@allure.feature("Pet API")
@allure.story("GET Pet")
class TestGetPet:
    @allure.title("Test getting a pet by ID")
    def test_get_pet_by_id(self, pet_id):
        get_pet_page = GetPetPage(pet_id)
        response = get_pet_page.send_request("GET")
        assert response.status_code == 200
        assert response.json()["id"] == pet_id

    @allure.title("Test getting a non-existent pet")
    def test_get_non_existent_pet(self):
        pet_id = 99999
        get_pet_page = GetPetPage(pet_id)
        response = get_pet_page.send_request("GET")
        assert response.status_code == 404

    @allure.title("Test getting a pet with invalid ID")
    def test_get_pet_with_invalid_id(self):
        pet_id = "invalid_id"
        get_pet_page = GetPetPage(pet_id)
        response = get_pet_page.send_request("GET")
        assert response.status_code == 404

    @allure.title("Test getting a pet with empty ID")
    def test_get_pet_with_empty_id(self):
        pet_id = ""
        get_pet_page = GetPetPage(pet_id)
        response = get_pet_page.send_request("GET")
        assert response.status_code == 405