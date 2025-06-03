import argparse
import json
import os
from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), 'appointments.json')

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def list_appointments(data):
    if not data:
        print('No appointments found.')
    else:
        for idx, appt in enumerate(data, start=1):
            print(f"{idx}. {appt['datetime']} - {appt['description']}")


def add_appointment(data, date_str, desc):
    try:
        dt = datetime.fromisoformat(date_str)
    except ValueError:
        print('Invalid date/time format. Use YYYY-MM-DDTHH:MM.')
        return
    data.append({'datetime': dt.isoformat(), 'description': desc})
    save_data(data)
    print('Appointment added.')


def remove_appointment(data, index):
    if 0 <= index < len(data):
        removed = data.pop(index)
        save_data(data)
        print(f"Removed appointment: {removed['datetime']} - {removed['description']}")
    else:
        print('Invalid index.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple appointment organizer')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('list', help='List appointments')

    add_parser = subparsers.add_parser('add', help='Add appointment')
    add_parser.add_argument('datetime', help='Date/time in YYYY-MM-DDTHH:MM format')
    add_parser.add_argument('desc', help='Description')

    rm_parser = subparsers.add_parser('remove', help='Remove appointment by number from list command')
    rm_parser.add_argument('index', type=int, help='Index starting at 1')

    args = parser.parse_args()
    data = load_data()

    if args.command == 'list':
        list_appointments(data)
    elif args.command == 'add':
        add_appointment(data, args.datetime, args.desc)
    elif args.command == 'remove':
        remove_appointment(data, args.index - 1)
    else:
        parser.print_help()
