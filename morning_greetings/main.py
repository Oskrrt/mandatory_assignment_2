import os
import sys

from morning_greetings.contact_manager import ContactsManager
from morning_greetings.logger import log_message_sent
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def main():
    ### get contacts
    cm = ContactsManager()
    cm.populate_contacts()
    contacts = cm.get_contacts()
    print(cm.contacts)
    cm.remove_contact("Emil")
    print("after removing emil")
    print(cm.contacts)
    cm.list_contacts()
    name = cm.get_contact_attribute(contacts[0], "name")
    print(name)
    email = cm.get_contact_attribute(contacts[0], "email")
    preferred_time = cm.get_contact_attribute(contacts[0], "preferred_time")
    print(name, email, preferred_time)

    ### send message
    try:
        send_message(cm.contacts[0])
    except ValueError as e:
        print(
            "Could not send message, make sure contacts exists in 'contacts.txt' with format: <name, email, preferred_time>")
    contact = {
        'name': 'roger',
        'email': 'roger@gmail.com',
        'preferred_time': '12:00'
    }


if __name__ == "__main__":
    main()
