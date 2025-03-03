import json
import mysql.connector
import os

def main():
    json_file_path = "../dataset/customer_data.json"

    if not os.path.exists(json_file_path):
        print(f"Không tìm thấy file {json_file_path}")
        return

    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            data_list = json.load(f)
            if not isinstance(data_list, list):
                print("Cấu trúc JSON không phải dạng list!")
                return
    except json.JSONDecodeError as e:
        print("File JSON không hợp lệ:", e)
        return

    try:
        conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="@Obama123",
            database="CustomerManagement"
        )
        cursor = conn.cursor()
    except mysql.connector.Error as err:
        print("Không thể kết nối MySQL:", err)
        return

    sql = """
    INSERT INTO customer (id, username, password, phone_number, email, name)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
       username=VALUES(username),
       password=VALUES(password),
       phone_number=VALUES(phone_number),
       email=VALUES(email),
       name=VALUES(name)
    """
    for user in data_list:
        val = (
            user.get("id", 0),
            user.get("username", ""),
            user.get("password", ""),
            user.get("phone_number", ""),
            user.get("email", ""),
            user.get("name", "")
        )
        try:
            cursor.execute(sql, val)
        except mysql.connector.Error as e:
            print(f"Lỗi khi chèn/cập nhật user {val}: {e}")

    conn.commit()
    cursor.close()
    conn.close()
    print("Đồng bộ JSON -> MySQL thành công!")

if __name__ == "__main__":
    main()
