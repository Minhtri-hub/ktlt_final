import os
import json

from libs.DataConnector import DataConnector
from model.Booking import Booking


def generate_sample_bookings():
    """Tạo dữ liệu mẫu cho bookings.json"""

    # Tìm thư mục gốc `ktlt_final`
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Lấy thư mục cha
    dataset_dir = os.path.join(base_dir, "dataset")  # Trỏ đến dataset trong ktlt_final
    os.makedirs(dataset_dir, exist_ok=True)  # Tạo thư mục nếu chưa có

    # Khởi tạo DataConnector với dataset_dir
    data_connector = DataConnector(dataset_dir)

    # Dữ liệu mẫu booking
    sample_bookings = [
        Booking(
            booking_id="B001",
            customer_id="C001",
            first_name="Alice",
            last_name="Nguyen",
            email="alice@example.com",
            mobile="+84 123456789",
            people=2,
            date="2025-04-15",
            time="6:30 PM",
            seating_type="Counter Seating",
            status="Confirmed",
            special_note="Anniversary dinner"
        ),
        Booking(
            booking_id="B002",
            customer_id="C002",
            first_name="Bob",
            last_name="Tran",
            email="bob@example.com",
            mobile="+84 987654321",
            people=4,
            date="2025-04-16",
            time="7:00 PM",
            seating_type="Private Dining",
            status="Pending",
            special_note="Vegetarian meal request"
        )
    ]

    # Chuyển đổi sang danh sách dictionary
    booking_data = [b.to_dict() for b in sample_bookings]

    # Lưu vào file JSON trong dataset/
    json_path = os.path.join(dataset_dir, "bookings.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(booking_data, f, indent=4)

    print(f"✅ Sample bookings saved to {json_path}")

if __name__ == "__main__":
    generate_sample_bookings()
