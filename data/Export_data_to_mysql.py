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

    sql_booking = """
    INSERT INTO booking (booking_id,full_name, email, mobile, special_note)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    for b in booking_list:
        val = (
            b.get("id", ""),
            b.get("full_name", ""),
            b.get("email", ""),
            b.get("mobile", ""),
            b.get("special_note", ""),
        )
        try:
            cursor.execute(sql_booking, val)
        except mysql.connector.Error as e:
            print(f"Lỗi khi chèn booking {val}: {e}")

    print("Đồng bộ booking_data.json -> MySQL (bảng booking) thành công!")


def sync_employee_data(cursor):
    json_file_path = "../dataset/employee_data.json"
    if not os.path.exists(json_file_path):
        print(f"Không tìm thấy file {json_file_path}")
        return

    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            employee_list = json.load(f)
            if not isinstance(employee_list, list):
                print("Cấu trúc JSON không phải dạng list!")
                return
    except json.JSONDecodeError as e:
        print("File JSON không hợp lệ:", e)
        return

    sql_employee = """
    INSERT INTO employee (
        EmployeeId, EmployeeName, EmployeeUsername, EmployeePass, hire_date, working_years, salary
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
       EmployeeName=VALUES(EmployeeName),
       EmployeeUsername=VALUES(EmployeeUsername),
       EmployeePass=VALUES(EmployeePass),
       hire_date=VALUES(hire_date),
       working_years=VALUES(working_years),
       salary=VALUES(salary)
    """

    for emp in employee_list:
        val = (
            emp.get("EmployeeId", 0),
            emp.get("EmployeeName", ""),
            emp.get("EmployeeUsername", ""),
            emp.get("EmployeePass", ""),
            emp.get("hire_date", ""),  # String date as per JSON
            emp.get("working_years", 0),
            emp.get("salary", 0)
        )
        try:
            cursor.execute(sql_employee, val)
        except mysql.connector.Error as e:
            print(f"Lỗi khi chèn/cập nhật nhân viên {val}: {e}")

    print("Đồng bộ employee_data.json -> MySQL (bảng employee) thành công!")



def sync_checktable_data(cursor):
    json_file_path = "../dataset/checktable_data.json"
    if not os.path.exists(json_file_path):
        print(f"Không tìm thấy file {json_file_path}")
        return

    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            checktable = json.load(f)
            if not isinstance(checktable, dict):
                print("Cấu trúc JSON không phải dạng dictionary!")
                return
    except json.JSONDecodeError as e:
        print("File JSON không hợp lệ:", e)
        return

    sql_checktable = """
    INSERT INTO checktable (date, id, time, people, type)
    VALUES (%s, %s, %s, %s, %s)
    """

    for date, data in checktable.items():  # Iterate over each date
        for entry in data.get("counter", []):  # Process "counter" group entries
            val = (
                date,  # Use the date key
                entry.get("id", 0),  # Extract "id"
                entry.get("time", ""),  # Extract "time"
                entry.get("people", 0),  # Extract "people"
                "counter"  # Set as "counter" type
            )
            try:
                cursor.execute(sql_checktable, val)
            except mysql.connector.Error as e:
                print(f"Lỗi khi chèn counter {val}: {e}")

        for entry in data.get("private", []):  # Process "private" group entries
            val = (
                date,  # Use the date key
                entry.get("id", 0),  # Extract "id"
                entry.get("time", ""),  # Extract "time"
                entry.get("people", 0),  # Extract "people"
                "private"  # Set as "private" type
            )
            try:
                cursor.execute(sql_checktable, val)
            except mysql.connector.Error as e:
                print(f"Lỗi khi chèn private {val}: {e}")

    print("Đồng bộ checktable_data.json -> MySQL (bảng checktable) thành công!")



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
    sync_employee_data(cursor)
    sync_checktable_data(cursor)

    conn.commit()
    cursor.close()
    conn.close()
    print("Hoàn tất đồng bộ JSON -> MySQL!")


if __name__ == "__main__":
    main()