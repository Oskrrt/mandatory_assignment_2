import os
import sys

from morning_greetings.contact_manager import ContactsManager
from morning_greetings.message_sender import send_message

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def main():
    ### get contacts
    cm = ContactsManager()
    cm.populate_contacts()
    contacts = cm.get_contacts()

    ### simulate message sending
    print("\n ----- SIMULATING AUTOMATION ----- \n")
    simulate_message_sending_automation(contacts)

    ### removal of contact
    test_remove(cm)

    ### adding new contact
    test_add(cm)


# test cases
# these are not actual unit tests, just functions to check functionality manually
def simulate_message_sending_automation(contacts):
    if not contacts:
        raise ValueError(
            "No contacts found, make sure 'contacts.txt' contains "
            "a contact with correct format:  <name, email, preferred_time>'")

    for contact in contacts:
        send_message(contact)


def test_add(cm):
    print("\n ----- Before adding new contact ----- \n")
    cm.list_contacts()
    cm.add_contact("erna", "erna_solberg@gmail.com", "07:00")
    print("\n ----- After adding new contact ----- \n")
    cm.list_contacts()


def test_remove(cm):
    print("\n ----- Before removal of Emil ----- \n")
    cm.list_contacts()
    cm.remove_contact_by_name("emil")
    print("\n ----- After Removal of Emil ----- \n")
    cm.list_contacts()


if __name__ == "__main__":
    main()
