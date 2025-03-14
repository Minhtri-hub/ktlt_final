import json
import os


def merge_checktable_and_booking():
    # File paths for the input and output files
    check_path = "../dataset/checktable_data.json"
    booking_path = "../dataset/booking_data.json"
    merged_path = "../dataset/merged_data.json"

    # Validate file existence
    if not os.path.exists(check_path):
        print("Không tìm thấy checktable_data.json! Vui lòng kiểm tra hoặc tạo file.")
        return
    if not os.path.exists(booking_path):
        print("Không tìm thấy booking_data.json! Vui lòng kiểm tra hoặc tạo file.")
        return

    # Load checktable_data.json
    try:
        with open(check_path, "r", encoding="utf-8") as f:
            check_data = json.load(f)
            if not isinstance(check_data, dict):  # Ensure it is a dictionary
                print("Invalid format: checktable_data.json must be a dictionary.")
                return
    except json.JSONDecodeError:
        print("Không thể đọc file checktable_data.json. Định dạng JSON không hợp lệ.")
        return

    # Load booking_data.json
    try:
        with open(booking_path, "r", encoding="utf-8") as f:
            booking_list = json.load(f)
            if not isinstance(booking_list, list):  # Ensure it is a list
                print("Invalid format: booking_data.json must be a list.")
                return
    except json.JSONDecodeError:
        print("Không thể đọc file booking_data.json. Định dạng JSON không hợp lệ.")
        return

    # Build a dictionary lookup for booking IDs
    booking_dict = {}
    for bk in booking_list:
        b_id = bk.get("id")
        if b_id is not None:  # Only include entries with valid IDs
            booking_dict[b_id] = bk

    merged_list = []

    # Process check_data, combining with matched data from booking_dict
    for date_str, seat_obj in check_data.items():
        for seat_type in ["counter", "private"]:
            if seat_type not in seat_obj:
                continue
            for item in seat_obj[seat_type]:
                # item = { "id": 1, "time": "4:00 PM", "people": 1 }
                c_id = item.get("id")
                if c_id in booking_dict:
                    bk_info = booking_dict[c_id]
                    # Merge item and booking info
                    merged_entry = {
                        "id": c_id,
                        "full_name": bk_info.get("full_name", ""),
                        "email": bk_info.get("email", ""),
                        "mobile": bk_info.get("mobile", ""),
                        "seat_type": seat_type,
                        "booking_time": item.get("time"),
                        "total_customers": item.get("people"),
                        "special_note": bk_info.get("special_note", ""),
                        "date": date_str,
                    }
                    merged_list.append(merged_entry)

    # Save the merged data to a new JSON file
    try:
        with open(merged_path, "w", encoding="utf-8") as f:
            json.dump(merged_list, f, indent=4, ensure_ascii=False)
        print(f"Đã merge {len(merged_list)} dòng vào {merged_path}")
    except Exception as e:
        print(f"Lỗi khi lưu dữ liệu vào {merged_path}: {e}")



if __name__ == "__main__":
    merge_checktable_and_booking()
