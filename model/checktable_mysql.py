import json
from data.mysql_connector import conn


def export_booking_to_checkdata_json():
    cursor = conn.cursor()
    # Truy vấn dữ liệu cần thiết từ MySQL
    sql = "SELECT booking_id, time, date, people FROM booking"
    cursor.execute(sql)
    dataset = cursor.fetchall()

    checkdata = {}

    for item in dataset:
        booking_date = item[2].strftime('%d/%m/%Y')
        time_formatted = item[1].strftime('%I:%M %p')

        # Nếu chưa có key cho ngày này, khởi tạo nó
        if booking_date not in checkdata:
            checkdata[booking_date] = {
                "counter": [],
                "private": []
            }

        checkdata[booking_date]["counter"].append({
            "id": item[0],  # booking_id
            "time": time_formatted,
            "people": item[3]  # Số lượng người
        })

    # Đường dẫn file JSON
    json_file_path = "../dataset/checkdata.json"
    with open(json_file_path, "w", encoding="utf-8") as json_file:
        json.dump(checkdata, json_file, indent=4, ensure_ascii=False)

    print(f"Dữ liệu booking đã được lưu vào {json_file_path}")
    cursor.close()


if __name__ == "__main__":
    export_booking_to_checkdata_json()
    conn.close()