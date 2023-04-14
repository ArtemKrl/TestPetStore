import allure
from pages.post_pet_page import PostPetPage
import pytest


@pytest.mark.run(order=1)
@allure.feature("Pet API")
@allure.story("POST Pet")
class TestPostPet:
    # проверка успешного создания нового животного
    @allure.title("Test creating a new pet")
    def test_create_pet(self, pet_data):
        post_pet_page = PostPetPage(pet_data)
        response = post_pet_page.send_request()
        assert response.status_code == 200
        assert response.json()["name"] == pet_data["name"]

    # проверка, что запрос на создание животного с невалидными данными возвращает ошибку 500
    @allure.title("Test creating a pet with invalid data")
    def test_create_pet_with_invalid_data(self):
        pet_data = {
            "id": "invalid_id",
            "category": {"id": "invalid_id", "name": "invalid_name"},
            "name": "Rufus",
            "photoUrls": "invalid_url",
            "tags": [{"id": "invalid_id", "name": "invalid_name"}],
            "status": "invalid_status"
        }
        post_pet_page = PostPetPage(pet_data)
        response = post_pet_page.send_request()
        assert response.status_code == 500

    # проверка, что запрос на создание животного с пустыми данными возвращает ошибку 405
    @allure.title("Test creating a pet with empty data")
    def test_create_pet_with_empty_data(self):
        pet_data = {"id": 1}
        post_pet_page = PostPetPage(pet_data)
        response = post_pet_page.send_request()
        assert response.status_code == 405

    # проверка, что запрос на создание животного с неполными данными возвращает ошибку 405
    @allure.title("Test creating a pet with incomplete data")
    def test_create_pet_with_incomplete_data(self):
        pet_data = {
            "id": 1,
            "name": "Rufus",
            "photoUrls": ["https://www.example.com"],
            "status": "available"
        }
        post_pet_page = PostPetPage(pet_data)
        response = post_pet_page.send_request()
        assert response.status_code == 405