from appointments import check_availability, book_appointment

print("--- Available slots on Monday ---")
print(check_availability("Monday"))

print("\n--- Booking an appointment ---")
result = book_appointment("Monday", "10:00", "Sara")
print(result)

print("\n--- Available slots on Monday after booking ---")
print(check_availability("Monday"))

print("\n--- Trying to book the same slot again ---")
result2 = book_appointment("Monday", "10:00", "Layla")
print(result2)