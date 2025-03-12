import sys
import os

from PyQt6.QtWidgets import QApplication, QMainWindow

from libs.DataConnector import DataConnector
from uiManagement.BookingManagementExt import BookingManagementExt

# Thêm thư mục cha vào `sys.path`
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def test_booking_management_window():
    # Xác định thư mục chứa dữ liệu JSON
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "dataset")
    data_connector = DataConnector(data_dir)

    # Tải danh sách booking từ JSON
    bookings = data_connector.load_bookings()
    if not bookings:
        print("No bookings found. Please add bookings data first.")
        return

    # Khởi tạo ứng dụng PyQt6
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()

    # Khởi tạo giao diện Booking Management
    booking_ui = BookingManagementExt(data_connector)
    booking_ui.setupUi(mainWindow)

    # Hiển thị cửa sổ
    mainWindow.show()

    # Chạy ứng dụng
    sys.exit(app.exec())

if __name__ == "__main__":
    test_booking_management_window()
