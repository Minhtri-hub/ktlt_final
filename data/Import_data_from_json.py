import json
import os


def get_data_from_json(file_name):
    """
    Đọc dữ liệu từ file JSON bất kỳ trong thư mục dataset.

    :param file_name: Tên file JSON cần đọc (VD: "employee_data.json")
    :return: Danh sách dữ liệu từ file hoặc [] nếu lỗi
    """
    json_file_path = os.path.join("..", "dataset", file_name)

    try:
        with open(json_file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        return data
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {file_name}!")
        return []
    except json.JSONDecodeError:
        print(f"Lỗi: File {file_name} bị lỗi hoặc không hợp lệ!")
        return []
