import json
from data.mysql_connector import conn


def export_booking_to_json():
    cursor = conn.cursor()
    # Query includes all fields including date and time
    sql = "SELECT booking_id, first_name, last_name, email, mobile, special_note, date, time FROM booking"
    cursor.execute(sql)
    dataset = cursor.fetchall()

    data_list = []
    for item in dataset:
        data_list.append({
            "booking_id": item[0],
            "first_name": item[1],
            "last_name": item[2],
            "email": item[3],
            "mobile": item[4],
            "special_note": item[5],
            "booking_date": item[6],  # Add date field from database
            "booking_time": item[7]  # Add time field from database
        })

    # Output JSON file path
    json_file_path = "../dataset/booking_data.json"
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(data_list, json_file, indent=4, ensure_ascii=False)

    print(f"Dữ liệu booking đã được lưu vào {json_file_path}")
    cursor.close()


if __name__ == "__main__":
    export_booking_to_json()
    conn.close()
