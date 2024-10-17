from logger import log_message_sent
from message_generator import generate_message


def send_message(contact):
    # simulates sending a message to the given contact with print()
    # message content is fetched from message_generator.generate_message()
    # logs the message sending event with generate_message()
    if not contact["name"]:
        raise ValueError("Name is missing")
    if not contact["email"]:
        raise ValueError("Email address is missing")
    message = generate_message(contact)
    print(f"Sending message to {contact['email']}: {message}")
    log_message_sent(contact, message)
