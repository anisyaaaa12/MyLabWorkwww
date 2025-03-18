# main.py
from flask import Flask, jsonify

# Создаем приложение Flask
app = Flask(__name__)

# Пример данных, которые будут возвращаться
data = {
    "message": "Hello, World!",
    "status": "success",
    "items": [
        {"id": 1, "name": "Item 1", "price": 10},
        {"id": 2, "name": "Item 2", "price": 20},
        {"id": 3, "name": "Item 3", "price": 30}
    ]
}

# Маршрут, который возвращает данные в формате JSON
@app.route('/api', methods=['GET'])
def get_data():
    return jsonify(data)

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
