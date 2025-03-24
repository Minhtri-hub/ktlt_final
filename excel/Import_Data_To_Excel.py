import pandas as pd
import os

# Dữ liệu JSON
data = [
    {
        "id": 1,
        "full_name": "Nguyễn Quách Minh Trí",
        "email": "nguyenquachminhtri@gmail.com",
        "mobile": "0903762652",
        "seat_type": "counter",
        "booking_time": "4:00 PM",
        "total_customers": 1,
        "special_note": "birthday",
        "date": "07/05/2025"
    },
    {
        "id": 2,
        "full_name": "Nguyễn Hoàng Nam",
        "email": "nguyenhoangnam@gmail",
        "mobile": "0903762652",
        "seat_type": "private",
        "booking_time": "6:15 PM",
        "total_customers": 1,
        "special_note": "anni 1 năm",
        "date": "04/04/2025"
    },
    {
        "id": 4,
        "full_name": "nhi",
        "email": "nhi@gmail.com",
        "mobile": "0903762652",
        "seat_type": "private",
        "booking_time": "5:00 PM",
        "total_customers": 25,
        "special_note": "birthday",
        "date": "01/05/2025"
    },
    {
        "id": 8,
        "full_name": "Nguyễn Huỳnh Yến Nhi",
        "email": "hnhi46@gmail.com",
        "mobile": "0903762652",
        "seat_type": "private",
        "booking_time": "8:00 PM",
        "total_customers": 3,
        "special_note": "Birthday 18 tuổi",
        "date": "01/05/2025"
    },
    {
        "id": 5,
        "full_name": "nguyễn minh đức",
        "email": "duc@gmail.com",
        "mobile": "090321456",
        "seat_type": "private",
        "booking_time": "6:00 PM",
        "total_customers": 9,
        "special_note": "birthday 20 tuổi",
        "date": "04/12/2025"
    },
    {
        "id": 6,
        "full_name": "Không tên",
        "email": "koten@gmail.com",
        "mobile": "09000000000",
        "seat_type": "counter",
        "booking_time": "5:45 PM",
        "total_customers": 9,
        "special_note": "annni",
        "date": "13/06/2025"
    },
    {
        "id": 7,
        "full_name": "m",
        "email": "m",
        "mobile": "m",
        "seat_type": "counter",
        "booking_time": "4:00 PM",
        "total_customers": 1,
        "special_note": "m",
        "date": "01/01/2025"
    },
    {
        "id": 9,
        "full_name": "Nguyễn Quách Minh Trí",
        "email": "tri@gmail.com",
        "mobile": "090654444122",
        "seat_type": "counter",
        "booking_time": "10:30 PM",
        "total_customers": 10,
        "special_note": "Anni",
        "date": "02/05/2025"
    }
]

# Chuyển dữ liệu JSON thành DataFrame
df = pd.DataFrame(data)

# Đảm bảo file được ghi ra thành CSV
file_path = os.path.abspath("reservations.csv")
try:
    # Xuất dữ liệu ra file CSV
    df.to_csv(file_path, index=False, encoding="utf-8-sig", sep=',')  # Sử dụng dấu phẩy làm phân cách
    print(f"Dữ liệu đã được xuất ra file '{file_path}' với từng dữ liệu tách vào ô riêng trong Excel.")
except PermissionError:
    print(f"Không thể ghi file. Hãy chắc chắn rằng '{file_path}' không bị mở hoặc bị khóa!")
except Exception as e:
    print(f"Lỗi xảy ra: {e}")
