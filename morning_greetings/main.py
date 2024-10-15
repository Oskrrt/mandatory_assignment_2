import morning_greetings
from setuptools import find_packages
import sys
import os

from morning_greetings import io_manager
from morning_greetings.contact_manager import ContactsManager
from morning_greetings.logger import log_message_2
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message

# Ensure the parent directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def main():
    contacts_path = os.path.join('resources', 'contacts.txt')
    logs_path = os.path.join('resources', 'message_logs.txt')
    print(contacts_path)

    ### get contacts from file
    contacts = io_manager.read_contacts_from_file(contacts_path)
    print(contacts)
    name = ContactsManager.get_contact_attribute(contacts[0], "name")
    email = ContactsManager.get_contact_attribute(contacts[0], "email")
    preferred_time = ContactsManager.get_contact_attribute(contacts[0], "preferred_time")
    print(name, email, preferred_time)
    ### generate messages
    message = generate_message(name)
    print(message)
    ### send messages
    send_message(email, message)
    ### logging
    log_message_2(contacts[0], message, logs_path)


if __name__ == "__main__":
    main()
