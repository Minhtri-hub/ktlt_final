from typing import List
from libs.JsonFilefactory import JsonFileFactory
from model.Booking import Booking
from model.Employee import Employee

class DataConnector:
    def __init__(self, data_dir: str = "data"):
        """Khởi tạo DataConnector với thư mục chứa dữ liệu"""
        self.json_factory = JsonFileFactory(data_dir)

    ### 🔹 QUẢN LÝ BOOKING ###
    def save_bookings(self, bookings: List[Booking]) -> bool:
        """Lưu danh sách booking vào JSON"""
        try:
            bookings_data = [booking.to_dict() for booking in bookings]
            return self.json_factory.write_json(bookings_data, "bookings.json")
        except Exception as e:
            print(f"Error saving bookings: {e}")
            return False

    def load_bookings(self) -> List[Booking]:
        """Đọc danh sách booking từ JSON"""
        try:
            bookings_data = self.json_factory.read_json("bookings.json")
            if bookings_data:
                return [Booking.from_dict(data) for data in bookings_data]
            return []
        except Exception as e:
            print(f"Error loading bookings: {e}")
            return []

    ### 🔹 QUẢN LÝ EMPLOYEE ###
    def save_employees(self, employees: List[Employee]) -> bool:
        """Lưu danh sách nhân viên vào JSON"""
        try:
            employees_data = [employee.to_dict() for employee in employees]
            return self.json_factory.write_json(employees_data, "employees.json")
        except Exception as e:
            print(f"Error saving employees: {e}")
            return False

    def load_employees(self) -> List[Employee]:
        """Đọc danh sách nhân viên từ JSON"""
        try:
            employees_data = self.json_factory.read_json("employees.json")
            if employees_data:
                return [Employee.from_dict(data) for data in employees_data]
            return []
        except Exception as e:
            print(f"Error loading employees: {e}")
            return []
