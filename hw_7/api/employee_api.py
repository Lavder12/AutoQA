import requests


class EmployeeApi:
    def __init__(self, base_url="http://5.101.50.27:8000"):
        self.base_url = base_url

    def create_employee(self, data):
        """Создание нового сотрудника"""
        url = f"{self.base_url}/employee/create"
        response = requests.post(url, json=data)
        return response

    def get_employee_info(self, employee_id):
        """Получение информации о сотруднике по ID"""
        url = f"{self.base_url}/employee/info"
        params = {"id": employee_id}
        response = requests.get(url, params=params)
        return response

    def update_employee(self, employee_id, changes):
        """Изменение данных сотрудника"""
        url = f"{self.base_url}/employee/change"
        data = {"id": employee_id, **changes}
        response = requests.patch(url, json=data)
        return response