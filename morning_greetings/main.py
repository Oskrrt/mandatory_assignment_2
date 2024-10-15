import os
import sys

from morning_greetings.contact_manager import ContactsManager
from morning_greetings.logger import log_message_2
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message

# Ensure the parent directory is in the Python path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def main():
    ### get contacts
    cm = ContactsManager()
    cm.populate_contacts()
    print(cm.contacts)
    cm.remove_contact("Emil")
    print("after removing emil")
    print(cm.contacts)
    cm.list_contacts()
    name = cm.get_contact_attribute(cm.contacts[0], "name")
    print(name)
    email = cm.get_contact_attribute(cm.contacts[0], "email")
    preferred_time = cm.get_contact_attribute(cm.contacts[0], "preferred_time")
    print(name, email, preferred_time)

    ### generate messages
    message = generate_message(name)
    print(message)
    ### send messages
    send_message(email, message)
    ### logging
    log_message_2(cm.contacts[0], message)


if __name__ == "__main__":
    main()
