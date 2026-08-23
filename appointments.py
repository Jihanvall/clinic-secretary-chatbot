import json
from database import init_db, get_booked_slots, add_appointment

init_db()

with open("data/clinic_schedule.json", "r") as f:
    CLINIC_DATA = json.load(f)

SCHEDULE = CLINIC_DATA["schedule"]


def check_availability(day: str) -> list[str]:
    """Return available time slots for a given day."""
    day = day.capitalize()
    booked = get_booked_slots()

    if day not in SCHEDULE:
        return []

    all_slots = [f"{day} {time}" for time in SCHEDULE[day]]
    available = [slot for slot in all_slots if slot not in booked]
    return available


def book_appointment(day: str, time: str, patient_name: str) -> str:
    """Book an appointment if the slot is available."""
    day = day.capitalize()
    slot = f"{day} {time}"
    booked = get_booked_slots()

    if day not in SCHEDULE or time not in SCHEDULE[day]:
        return f"Sorry, {slot} is not a valid slot."
    if slot in booked:
        return f"Sorry, {slot} is already booked."

    add_appointment(day, time, patient_name)
    return f"Appointment booked for {patient_name} on {slot}."


def get_clinic_info() -> dict:
    """Return general clinic information."""
    return CLINIC_DATA["clinic_info"]