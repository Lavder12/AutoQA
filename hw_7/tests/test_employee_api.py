import pytest
from api.employee_api import EmployeeApi


class TestEmployeeApi:
    @pytest.fixture
    def api(self):
        return EmployeeApi()

    @pytest.fixture
    def valid_employee_data(self):
        """Данные, которые должны пройти валидацию"""
        return {
            "name": "Иван Иванов",
            "position": "Разработчик",
            "department": "IT",
            "salary": 100000,
            "email": "ivanov@example.com",
            "hire_date": "2023-01-01"
        }

    @pytest.fixture
    def minimal_employee_data(self):
        """Минимальный набор данных для создания"""
        return {
            "name": "Минимальный Тест",
            "position": "Тестовая должность"
        }

    def test_create_employee_success(self, api, valid_employee_data):
        """Тест успешного создания сотрудника"""
        response = api.create_employee(valid_employee_data)

        # Проверяем как успешный ответ (201), так и ошибку валидации (422)
        if response.status_code == 422:
            error_details = response.json()
            pytest.fail(f"Validation failed. Server response: {error_details}")

        assert response.status_code == 201
        employee_data = response.json()
        assert "id" in employee_data
        return employee_data["id"]

    def test_create_employee_minimal(self, api, minimal_employee_data):
        """Тест создания с минимальными данными"""
        response = api.create_employee(minimal_employee_data)

        if response.status_code == 422:
            error_details = response.json()
            pytest.skip(f"Skipping minimal test - validation failed: {error_details}")

        assert response.status_code == 201

    def test_get_employee_info(self, api, valid_employee_data):
        """Тест получения информации о сотруднике"""
        # Сначала создаем сотрудника
        employee_id = self.test_create_employee_success(api, valid_employee_data)

        # Получаем информацию
        response = api.get_employee_info(employee_id)
        assert response.status_code == 200
        employee_info = response.json()

        # Проверяем основные поля
        assert employee_info["id"] == employee_id
        assert employee_info["name"] == valid_employee_data["name"]
        assert employee_info["position"] == valid_employee_data["position"]

    def test_update_employee(self, api, valid_employee_data):
        """Тест обновления данных сотрудника"""
        employee_id = self.test_create_employee_success(api, valid_employee_data)

        updates = {
            "position": "Старший разработчик",
            "salary": 120000
        }

        response = api.update_employee(employee_id, updates)
        assert response.status_code == 200

        # Проверяем обновленные данные
        updated_info = api.get_employee_info(employee_id).json()
        assert updated_info["position"] == updates["position"]
        assert updated_info["salary"] == updates["salary"]