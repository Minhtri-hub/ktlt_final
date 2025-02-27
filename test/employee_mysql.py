import json
from data.mysql_connector import conn

cursor = conn.cursor()

# Truy vấn dữ liệu từ bảng employee
sql = "SELECT EmployeeId, EmployeeName, EmployeeUsername, EmployeePass FROM employee"
cursor.execute(sql)
dataset = cursor.fetchall()

# Chuyển đổi dữ liệu thành danh sách các dict
data_list = []
for item in dataset:
    data_list.append({
        "EmployeeId": item[0],
        "EmployeeName": item[1],
        "EmployeeUsername": item[2],
        "EmployeePass": item[3]  # Có thể mã hóa mật khẩu ở đây nếu cần
    })

# Lưu dữ liệu vào file JSON
json_file_path = "../dataset/employee_data.json"
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(data_list, json_file, indent=4, ensure_ascii=False)

print(f"Dữ liệu nhân viên đã được lưu vào {json_file_path}")

cursor.close()
