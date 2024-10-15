from io_manager import read_contacts_from_file


class ContactsManager:
    def __init__(self):
        self.contacts = []

    @staticmethod
    def separate_contact_attributes(contact):
        ### helper method to avoid duplicate code, might need to use this multiple places
        ### contact = string with the attributes seperated by comma
        ### return an array with each attribute for the contact
        return contact.replace(" ", "").split(",")

    def get_contact_attribute(self, contact, attribute):
        return contact[attribute]

    def populate_contacts(self):
        contacts_from_file = read_contacts_from_file()
        print("contacts from file:")
        print(contacts_from_file)
        for contact in contacts_from_file:
            contact_as_array = ContactsManager.separate_contact_attributes(contact)
            contact_dict = {
                'name': contact_as_array[0],
                'email': contact_as_array[1],
                'preferred_time': contact_as_array[2],
            }
            self.contacts.append(contact_dict)

    def add_contact_to_file(self, contact):
        return

    def add_contact(self, name, email, preferred_time="08:00 AM"):
        contact = {
            'name': name,
            'email': email,
            'preferred_time': preferred_time
        }
        self.contacts.append(contact)

    def remove_contact(self, name):
        self.contacts = [c for c in self.contacts if c['name'] != name.lower()]

    def get_contacts(self):
        return self.contacts

    def list_contacts(self):
        for contact in self.contacts:
            print(
                f"Name: {contact['name'].title()}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")
