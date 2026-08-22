# Temporary in-memory storage (we'll replace with a real database later)
booked_appointments = []

AVAILABLE_SLOTS = [
    "Monday 10:00",
    "Monday 15:00",
    "Tuesday 11:00",
    "Tuesday 17:00",
    "Wednesday 09:00",
]


def check_availability(day: str) -> list[str]:
    """Return available time slots for a given day."""
    day = day.capitalize()
    slots = [slot for slot in AVAILABLE_SLOTS if slot.startswith(day)]
    slots = [slot for slot in slots if slot not in booked_appointments]
    return slots


def book_appointment(day: str, time: str, patient_name: str) -> str:
    """Book an appointment if the slot is available."""
    slot = f"{day.capitalize()} {time}"
    if slot not in AVAILABLE_SLOTS:
        return f"Sorry, {slot} is not a valid slot."
    if slot in booked_appointments:
        return f"Sorry, {slot} is already booked."
    booked_appointments.append(slot)
    return f"Appointment booked for {patient_name} on {slot}."