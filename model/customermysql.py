import json
from data.mysql_connector import conn

cursor = conn.cursor()

# Truy vấn dữ liệu từ bảng customer
sql = "SELECT * FROM customer"
cursor.execute(sql)
dataset = cursor.fetchall()

# Chuyển đổi dữ liệu thành danh sách các dict
data_list = []
for item in dataset:
    data_list.append({
        "id": item[0],
        "username": item[1],
        "password": item[2],
        "phone_number":item[3],
        "email":item[4],
        "name": item[5]
    })


json_file_path = "../dataset/customer_data.json"
with open(json_file_path, "w", encoding="utf-8") as json_file:
    json.dump(data_list, json_file, indent=4, ensure_ascii=False)

print(f"Dữ liệu đã được lưu vào {json_file_path}")

cursor.close()
