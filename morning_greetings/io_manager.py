import datetime
import os

# For some reason this path seems to work differently on my home computer
# and my laptop, even though it is cloned the same way, and the file
# structure is the same. The commented out line is the correct one for my home
# computer, while the other is correct for my laptop. Adjust this accordingly.

# CONTACTS_FILE_PATH = os.path.join('resources', 'contacts.txt')
CONTACTS_FILE_PATH = os.path.join('..', 'resources', 'contacts.txt')
LOGS_FILE_PATH = os.path.join('..', 'resources', 'message_logs.txt')


def log_message_to_file(contact, message, file_name):
    try:
        with open(file_name, "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - Sent to {contact['name']}: {message}\n")
    except FileNotFoundError as e:
        print("File not found: " + e.filename)


def log_message_to_file_2(contact, message):
    try:
        with open(LOGS_FILE_PATH, "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - Sent to {contact['name']}: {message}\n")
    except FileNotFoundError as e:
        print("File not found: " + e.filename)


def read_contacts_from_file():
    try:
        with open(CONTACTS_FILE_PATH, "r") as contact_file:
            lines = [line.rstrip() for line in contact_file]
        return lines
    except FileNotFoundError as e:
        print("File not found: " + e.filename)


def write_contact_to_file():
    try:
        with open(CONTACTS_FILE_PATH, "a") as contact_file:
            lines = [line.rstrip() for line in contact_file]
        return lines
    except FileNotFoundError as e:
        print("File not found: " + e.filename)


def remove_contact_from_file():
    try:
        with open(CONTACTS_FILE_PATH, "r+") as contact_file:
            d = contact_file.readlines()
            contact_file.seek(0)
            for line in d:
                if line != "line you want to remove...":
                    contact_file.write(line)
            contact_file.truncate()
    except FileNotFoundError as e:
        print("File not found: " + e.filename)
