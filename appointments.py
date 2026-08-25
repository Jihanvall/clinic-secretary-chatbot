import json
from database import init_db, get_booked_slots, add_appointment, cancel_appointment, find_appointment

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

def get_treatments() -> list[str]:
    """Return the list of treatment types offered by the clinic."""
    return CLINIC_DATA["treatments"]

def cancel_booking(day: str, time: str) -> str:
    """Cancel an existing appointment."""
    day = day.capitalize()
    slot = f"{day} {time}"

    if not find_appointment(day, time):
        return f"Sorry, there is no appointment booked for {slot}."

    cancel_appointment(day, time)
    return f"Your appointment on {slot} has been cancelled."


def reschedule_booking(old_day: str, old_time: str, new_day: str, new_time: str, patient_name: str) -> str:
    """Cancel an existing appointment and book a new one instead."""
    old_day = old_day.capitalize()
    new_day = new_day.capitalize()

    if not find_appointment(old_day, old_time):
        return f"Sorry, there is no appointment booked for {old_day} {old_time} to reschedule."

    new_slot = f"{new_day} {new_time}"
    booked = get_booked_slots()

    if new_day not in SCHEDULE or new_time not in SCHEDULE[new_day]:
        return f"Sorry, {new_slot} is not a valid slot."
    if new_slot in booked:
        return f"Sorry, {new_slot} is already booked."

    cancel_appointment(old_day, old_time)
    add_appointment(new_day, new_time, patient_name)
    return f"Your appointment has been moved from {old_day} {old_time} to {new_slot}."