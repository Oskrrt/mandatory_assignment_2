import datetime


def log_message_to_file(contact, message, file_name):
    with open(file_name, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {contact['name']}: {message}\n")


def log_message_to_file_2(contact, message, file_name):
    with open(file_name, "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {contact}: {message}\n")


def read_contacts_from_file(file_name):
    with open(file_name, "r") as contact_file:
        lines = [line.rstrip() for line in contact_file]

    return lines
