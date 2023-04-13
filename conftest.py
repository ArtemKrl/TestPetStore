import pytest

@pytest.fixture(scope="class")
def pet_id():
    return 2  # здесь можно задать id животного, которое существует в базе данных

@pytest.fixture(scope="class")
def pet_data():
    return {
        "id": 1,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Rufus",
        "photoUrls": ["https://www.example.com"],
        "tags": [{"id": 1, "name": "tag1"}],
        "status": "available"
        }