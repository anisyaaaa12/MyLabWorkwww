# test_main.py
import pytest
from main import app

# Создаем клиент для тестирования
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Тест на проверку статуса и структуры данных
def test_get_data(client):
    # Отправляем GET-запрос на /api
    response = client.get('/api')
    
    # Проверяем, что статус-код ответа 200
    assert response.status_code == 200
    
    # Проверяем, что данные в ответе соответствуют ожидаемому формату
    json_data = response.get_json()
    assert json_data['status'] == 'success'
    assert 'items' in json_data
    assert len(json_data['items']) == 3
