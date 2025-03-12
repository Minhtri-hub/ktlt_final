from dataclasses import dataclass
from typing import Optional

@dataclass
class Booking:
    booking_id: str
    customer_id: str
    first_name: str
    last_name: str
    email: str
    mobile: str
    people: int
    date: str
    time: str
    seating_type: str  # Counter Seating / Private Dining
    status: str  # Confirmed / Pending / Cancelled
    special_note: Optional[str] = ""

    def to_dict(self):
        """Chuyển Booking thành dictionary để lưu JSON"""
        return {
            "booking_id": self.booking_id,
            "customer_id": self.customer_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "mobile": self.mobile,
            "people": self.people,
            "date": self.date,
            "time": self.time,
            "seating_type": self.seating_type,
            "status": self.status,
            "special_note": self.special_note
        }

    @classmethod
    def from_dict(cls, data):
        """Tạo Booking từ dictionary (đọc từ JSON)"""
        return cls(
            booking_id=data["booking_id"],
            customer_id=data["customer_id"],
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            mobile=data["mobile"],
            people=data["people"],
            date=data["date"],
            time=data["time"],
            seating_type=data["seating_type"],
            status=data["status"],
            special_note=data.get("special_note", "")
        )
