import datetime
import os
from os import getcwd

CONTACTS_FILE_PATH = os.path.join('morning_greetings', 'resources', 'contacts.txt')
LOGS_FILE_PATH = os.path.join('morning_greetings', 'resources', 'message_logs.txt')


def log_message_sent_to_file(contact, message):
    # logs the message sending event to resources/message_logs.txt
    try:
        with open(LOGS_FILE_PATH, "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - Message sent to {contact['name']}: {message}\n")
    except FileNotFoundError as e:
        print("File not found: " + e.filename)
        raise e


def log_message_generated_to_file(contact, message):
    # logs the message generation event to resources/message_logs.txt
    try:
        with open(LOGS_FILE_PATH, "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - Message generated for {contact['name']}: {message}\n")
    except FileNotFoundError as e:
        print("File not found: " + e.filename)
        raise e


def read_contacts_from_file():
    # reads all contacts from resources/contacts.txt
    # returns a list of the contacts found
    try:
        with open(CONTACTS_FILE_PATH, "r") as contact_file:
            lines = [line.rstrip() for line in contact_file]
        return lines
    except FileNotFoundError as e:
        print("File not found: " + e.filename)


def write_contact_to_file(contact):
    # Appends the contact to resources/contacts.txt
    try:
        with open(CONTACTS_FILE_PATH, "a") as contact_file:
            contact_file.write(f"{contact['name']}, {contact['email']}, {contact['preferred_time']}\n")
    except FileNotFoundError as e:
        print("File not found: " + e.filename)


def remove_contact_from_file():
    # Removes the contact from resources/contacts.txt
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
