import json
import os
import mysql.connector
from datetime import datetime


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


import os
import json
import mysql.connector


def sync_booking_data(cursor):
    json_file_path = "../dataset/booking_data.json"

    # Check if the JSON file exists
    if not os.path.exists(json_file_path):
        print(f"Không tìm thấy file {json_file_path}")
        return

    # Load JSON data
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
    INSERT INTO booking (booking_id, full_name, email, mobile, special_note)
    VALUES (%s, %s, %s, %s, %s)
    """

    for b in booking_list:
        # Prepare values with fallback defaults for safety
        val = (
            b.get("id"),
            b.get("full_name", ""),
            b.get("email", ""),
            b.get("mobile", ""),
            b.get("special_note", ""),
        )

        # Check if 'id' is None or invalid
        if val[0] is None:
            print(f"Bỏ qua booking do thiếu 'id': {b}")
            continue  # Skip records with missing ID

        try:
            # Attempt to execute the SQL query
            cursor.execute(sql_booking, val)
        except mysql.connector.IntegrityError as e:
            print(f"Lỗi ràng buộc khi chèn booking {val}: {e}")
        except mysql.connector.DataError as e:
            print(f"Lỗi dữ liệu khi chèn booking {val}: {e}")
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

    for date, data in checktable.items():
        try:
            formatted_date = datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
        except ValueError:
            formatted_date = None

        for entry in data.get("counter", []):
            try:
                formatted_time = datetime.strptime(entry.get("time", ""), "%I:%M %p").strftime("%H:%M:%S") if entry.get("time") else None
            except ValueError:
                formatted_time = None

            val = (
                formatted_date,
                entry.get("id"),
                formatted_time,
                entry.get("people"),
                "counter"
            )
            try:
                cursor.execute(sql_checktable, val)
            except mysql.connector.Error as e:
                print(f"Lỗi khi chèn counter {val}: {e}")

        for entry in data.get("private", []):
            try:
                formatted_time = datetime.strptime(entry.get("time", ""), "%I:%M %p").strftime("%H:%M:%S") if entry.get("time") else None
            except ValueError:
                formatted_time = None

            val = (
                formatted_date,
                entry.get("id"),
                formatted_time,
                entry.get("people"),
                "private"
            )
            try:
                cursor.execute(sql_checktable, val)
            except mysql.connector.Error as e:
                print(f"Lỗi khi chèn private {val}: {e}")

    print("Đồng bộ checktable_data.json -> MySQL (bảng checktable) thành công!")




def sync_reservation_data(cursor):
    json_file_path = "../dataset/reservation_data.json"

    if not os.path.exists(json_file_path):
        print(f"Không tìm thấy file {json_file_path}")
        return

    try:
        with open(json_file_path, "r", encoding="utf-8") as f:
            reservation_list = json.load(f)
            if not isinstance(reservation_list, list):
                print("Cấu trúc JSON không phải dạng list!")
                return
    except json.JSONDecodeError as e:
        print("File JSON không hợp lệ:", e)
        return

    sql_reservation = """
    INSERT INTO reservation (id, full_name, email, mobile, seat_type, booking_time, total_customers, special_note, date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
       full_name=VALUES(full_name),
       email=VALUES(email),
       mobile=VALUES(mobile),
       seat_type=VALUES(seat_type),
       booking_time=VALUES(booking_time),
       total_customers=VALUES(total_customers),
       special_note=VALUES(special_note),
       date=VALUES(date)
    """

    for res in reservation_list:
        # Convert 'date' field to MySQL-compatible format
        try:
            res_date = datetime.strptime(res.get("date", ""), "%d/%m/%Y").strftime("%Y-%m-%d") if res.get(
                "date") else None
        except ValueError:
            print(f"Lỗi định dạng ngày không hợp lệ: {res.get('date')}")
            res_date = None

        # Convert 'booking_time' field to MySQL-compatible 24-hour format
        try:
            res_time = datetime.strptime(res.get("booking_time", ""), "%I:%M %p").strftime("%H:%M:%S") if res.get(
                "booking_time") else None
        except ValueError:
            print(f"Lỗi định dạng giờ không hợp lệ: {res.get('booking_time')}")
            res_time = None

        # Preparing reservation values for database insertion
        val = (
            res.get("id"),
            res.get("full_name"),
            res.get("email"),
            res.get("mobile"),
            res.get("seat_type"),
            res_time,
            res.get("total_customers"),
            res.get("special_note"),
            res_date
        )

        # Insert reservation and handle potential database errors
        try:
            cursor.execute(sql_reservation, val)
        except mysql.connector.Error as e:
            print(f"Lỗi khi chèn/cập nhật reservation {val}: {e}")

    print("Đồng bộ reservation_data.json -> MySQL (bảng reservation) thành công!")


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
    sync_reservation_data(cursor)

    conn.commit()
    cursor.close()
    conn.close()
    print("Hoàn tất đồng bộ JSON -> MySQL!")


if __name__ == "__main__":
    main()