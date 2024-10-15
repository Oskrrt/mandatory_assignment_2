from io_manager import log_message_to_file, log_message_to_file_2


def log_message(contact, message, file_name):
    log_message_to_file(contact, message, file_name)


def log_message_2(contact, message):
    log_message_to_file_2(contact, message)
    print("Message logged")
