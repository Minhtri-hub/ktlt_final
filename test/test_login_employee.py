import getpass
from data.Import_data_from_json import get_data_from_json


file_name = input("Nhập tên file JSON chứa dữ liệu đăng nhập (VD: employee_data.json): ").strip()

# Đọc dữ liệu từ file JSON
users = get_data_from_json(file_name)

if not users:
    print("Không thể tải dữ liệu. Thoát chương trình!")
    exit()

username_key = None
password_key = None
name_key = None

# Xác định khóa username và password từ file JSON (tự động nhận diện)
for key in users[0].keys():
    if "user" in key.lower():
        username_key = key
    elif "pass" in key.lower():
        password_key = key
    elif "name" in key.lower():
        name_key = key

# Nếu không tìm thấy trường cần thiết, báo lỗi
if not username_key or not password_key:
    print("❌ Lỗi: Không tìm thấy trường Username hoặc Password trong file JSON!")
    exit()

# Nhập thông tin đăng nhập
username_input = input("Nhập Username: ")
password_input = getpass.getpass("Nhập Password: ")  # Ẩn mật khẩu khi nhập

# Kiểm tra thông tin đăng nhập
authenticated = False
user_name = ""

for user in users:
    if user[username_key] == username_input and user[password_key] == password_input:
        authenticated = True
        user_name = user[name_key] if name_key else username_input  # Nếu có trường tên thì dùng, không thì lấy username
        break

# Xuất kết quả
if authenticated:
    print(f"Đăng nhập thành công! Chào mừng {user_name} ")
else:
    print("Sai Username hoặc Password! Vui lòng thử lại.")
