from io_manager import read_contacts_from_file, write_contact_to_file


class ContactsManager:
    def __init__(self):
        self.contacts = []

    @staticmethod
    def separate_contact_attributes(contact):
        # helper method to avoid duplicate code, might need to use this multiple places
        # contact = string with the attributes seperated by comma
        # return a list with each attribute for the contact
        return contact.replace(" ", "").split(",")

    def get_contact_attribute(self, contact, attribute):
        # returns the value of the given contact's attribute
        return contact[attribute]

    def populate_contacts(self):
        # populates the self.contacts[] list from the contents of resources/contacts.txt
        # un-comment the contacts_from_file = [] line to force error for manual testing
        contacts_from_file = read_contacts_from_file()
        # contacts_from_file = []
        if not contacts_from_file:
            raise ValueError(
                "No contacts found, make sure 'contacts.txt' contains "
                "a contact with correct format:  <name, email, preferred_time>'")

        for contact in contacts_from_file:
            contact_as_list = ContactsManager.separate_contact_attributes(contact)
            contact_dict = {
                'name': contact_as_list[0],
                'email': contact_as_list[1],
                'preferred_time': contact_as_list[2],
            }
            self.contacts.append(contact_dict)

    def add_contact_to_file(self, contact):
        write_contact_to_file(contact)

    def add_contact(self, name, email, preferred_time="08:00"):
        contact = {
            'name': name,
            'email': email,
            'preferred_time': preferred_time
        }
        self.contacts.append(contact)

    def remove_contact_by_name(self, name):
        self.contacts = [c for c in self.contacts if c['name'] != name.lower()]

    def remove_contact_by_email(self, email):
        self.contacts = [c for c in self.contacts if c['email'] != email.lower()]

    def get_contacts(self):
        return self.contacts

    def list_contacts(self):
        for contact in self.contacts:
            print(
                f"Name: {contact['name'].title()}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")
