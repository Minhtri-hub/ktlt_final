from data.mysql_connector import conn
import mysql.connector

try:
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    print("Danh sách bảng:", tables)
except mysql.connector.Error as err:
    print("Lỗi truy vấn:", err)
