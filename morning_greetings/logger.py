from io_manager import log_message_generated_to_file, log_message_sent_to_file


def log_message_sent(contact, message):
    try:
        log_message_sent_to_file(contact, message)
        print("Message sending event logged")
    except FileNotFoundError as e:
        print("Could not log message sending event")


def log_message_generated(contact, message):
    try:
        log_message_generated_to_file(contact, message)
        print("Message generation event logged")
    except FileNotFoundError as e:
        print("Could not log message generation event")
