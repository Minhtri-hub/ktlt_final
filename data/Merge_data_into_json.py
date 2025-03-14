import json
import os


def merge_data(checktable_path, booking_path, merged_path):
    # Ensure paths exist
    if not os.path.exists(checktable_path) or not os.path.exists(booking_path):
        print("Input files not found!")
        return

    # Load checktable data
    with open(checktable_path, "r", encoding="utf-8") as f:
        try:
            checktable_data = json.load(f)
        except json.JSONDecodeError:
            print("Error reading checktable_data.json")
            return

    # Add source tag to checktable entries
    for date, seat_types in checktable_data.items():
        for seat_type, seats in seat_types.items():
            for seat in seats:
                seat["source"] = "checktable"  # Mark as coming from checktable

    # Load booking data
    with open(booking_path, "r", encoding="utf-8") as f:
        try:
            booking_data = json.load(f)
        except json.JSONDecodeError:
            print("Error reading booking_data.json")
            return

    # Prepare a merged result
    merged_data = checktable_data.copy()  # Start with checktable data structure

    # Traverse through booking data and merge
    for booking in booking_data:
        booking_id = booking["id"]  # Extract booking ID
        booking_date = f'Booking date:{booking["date"]}'
        seat_type = booking.get("seat_type", "private")  # Default to "private" if not specified

        if booking_date not in merged_data:
            merged_data[booking_date] = {"counter": [], "private": []}

        # Find the corresponding seat type and check for matching ID in the correct category
        seat_list = merged_data[booking_date][seat_type]
        updated = False

        for seat in seat_list:
            if seat["id"] == booking_id:
                # Merge booking details into the checktable entry
                seat.update({
                    "first_name": booking.get("first_name", ""),
                    "last_name": booking.get("last_name", ""),
                    "email": booking.get("email", ""),
                    "mobile": booking.get("mobile", ""),
                    "special_note": booking.get("special_note", ""),
                    "source": "booking",  # Mark this entry as updated by booking,
                    "time": f"Booking Time: {booking['time']}"  # Annotate as Booking Time
                })
                updated = True
                break

        if not updated:
            # If no matching ID is found, add this booking as a new entry
            seat_list.append({
                "id": booking_id,
                "time": f"Booking Time: {booking['time']}",  # Annotate as Booking Time
                "first_name": booking.get("first_name", ""),
                "last_name": booking.get("last_name", ""),
                "email": booking.get("email", ""),
                "mobile": booking.get("mobile", ""),
                "special_note": booking.get("special_note", ""),
                "source": "booking"  # Mark this new entry as added by booking
            })

    # Save merged result
    os.makedirs(os.path.dirname(merged_path), exist_ok=True)
    with open(merged_path, "w", encoding="utf-8") as f:
        json.dump(merged_data, f, indent=4, ensure_ascii=False)
    print(f"Merged data saved to {merged_path}")

    # Print details of merged data with source information for debugging/checking
    for date, seat_types in merged_data.items():
        print(f"Date: {date}")
        for seat_type, seats in seat_types.items():
            print(f"  Seat Type: {seat_type}")
            for seat in seats:
                print(f"    {seat['time']}, Source: {seat['source']}")


# Example usage
merge_data(
    "../dataset/checktable_data.json",
    "../dataset/booking_data.json",
    "../dataset/merged_data.json"
)
