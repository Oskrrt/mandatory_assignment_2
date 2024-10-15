from logger import log_message
from message_generator import generate_message


def send_message(email, message):
    if not email:
        raise ValueError("Email address is missing")

    print(f"Sending message to {email}: {message}")
