import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from appointments import check_availability, book_appointment, cancel_booking


def test_check_availability_returns_list():
    slots = check_availability("Monday")
    assert isinstance(slots, list)


def test_book_appointment_success():
    slots_before = check_availability("Wednesday")
    if not slots_before:
        pytest.skip("No available Wednesday slots to test booking")

    day, time = "Wednesday", slots_before[0].split(" ")[1]
    result = book_appointment(day, time, "Test Patient")

    assert "booked" in result.lower()

    cancel_booking(day, time)  # cleanup


def test_book_appointment_invalid_slot():
    result = book_appointment("Monday", "23:59", "Test Patient")
    assert "not a valid slot" in result.lower()


def test_cancel_nonexistent_appointment():
    result = cancel_booking("Monday", "23:59")
    assert "no appointment booked" in result.lower()