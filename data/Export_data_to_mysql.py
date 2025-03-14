import json
import os
import mysql.connector

def sync_customer_data(cursor):
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

    sql_customer = """
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
            cursor.execute(sql_customer, val)
        except mysql.connector.Error as e:
            print(f"Lỗi khi chèn/cập nhật user {val}: {e}")

    print("Đồng bộ customer_data.json -> MySQL (bảng customer) thành công!")

def sync_booking_data(cursor):
    json_file_path = "../dataset/booking_data.json"
    if not os.path.exists(json_file_path):
        print(f"Không tìm thấy file {json_file_path}")
        return

    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            booking_list = json.load(f)
            if not isinstance(booking_list, list):
                print("Cấu trúc JSON không phải dạng list!")
                return
    except json.JSONDecodeError as e:
        print("File JSON không hợp lệ:", e)
        return

    # Insert statement now includes all placeholders for columns: first_name, last_name, email, mobile, special_note, date, time
    sql_booking = """
    INSERT INTO booking (first_name, last_name, email, mobile, special_note, date, time)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    for b in booking_list:
        # Each value must correspond to a column in the SQL query
        val = (
            b.get("first_name", ""),
            b.get("last_name", ""),
            b.get("email", ""),
            b.get("mobile", ""),
            b.get("special_note", ""),
            b.get("date", "0000-00-00"),  # Default value for date
            b.get("time", "00:00:00")  # Default value for time
        )
        try:
            cursor.execute(sql_booking, val)
        except mysql.connector.Error as e:
            print(f"Lỗi khi chèn booking {val}: {e}")

    print("Đồng bộ booking_data.json -> MySQL (bảng booking) thành công!")

def main():
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

    sync_customer_data(cursor)
    sync_booking_data(cursor)

    conn.commit()
    cursor.close()
    conn.close()
    print("Hoàn tất đồng bộ JSON -> MySQL!")

if __name__ == "__main__":
    main()
