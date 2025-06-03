# Appointment Organizer App

This simple command-line application lets you store and manage a list of appointments.
It is written in Python and stores appointments in a JSON file (`appointments.json`).

## Features

- **List** all appointments.
- **Add** a new appointment with a date/time and description.
- **Remove** an appointment by its list number.

## Usage

1. Ensure you have Python 3 installed.
2. Run the script with one of the commands below:

```bash
# Show all appointments
python appointment_app/app.py list

# Add an appointment (format: YYYY-MM-DDTHH:MM)
python appointment_app/app.py add 2024-05-01T14:30 "Doctor visit"

# Remove the first appointment
python appointment_app/app.py remove 1
```

The data is stored in `appointment_app/appointments.json` next to the script.
