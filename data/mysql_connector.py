import mysql.connector

server = "localhost"
port = 3306
database = "CustomerManagement"
username = "root"
password = "@Obama123"

try:
    conn = mysql.connector.connect(
        host=server,
        port=port,
        database=database,
        user=username,
        password=password
    )
    if conn.is_connected():
        print("Kết nối MySQL thành công!")
except mysql.connector.Error as err:
    print(f"Không thể kết nối MySQL: {err}")
    exit(1)
