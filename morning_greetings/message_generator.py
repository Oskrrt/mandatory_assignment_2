from morning_greetings.logger import log_message_generated
from datetime import datetime


def generate_message(contact):
    # generates the message
    sub_message = generate_sub_message_based_on_time(contact['preferred_time'])
    message = f"Good {sub_message[0]}, {contact['name'].title()}! {sub_message[1]}"
    log_message_generated(contact, message)
    return message


def generate_sub_message_based_on_time(time):
    # generate conditional content for the message based on the contact's preferred_time
    # change time from string to int
    time = datetime.strptime(time, "%H:%M").hour
    conditional_message_content = []
    if time <= 5:
        conditional_message_content.append("night")
        conditional_message_content.append("should you not be sleeping?")
    elif time <= 9:
        conditional_message_content.append("morning")
        conditional_message_content.append("Have a great day early bird!")
    elif time <= 12:
        conditional_message_content.append("morning")
        conditional_message_content.append("Have a great day!")
    elif time <= 18:
        conditional_message_content.append("afternoon")
        conditional_message_content.append("Have a great rest of the day!")
    else:
        conditional_message_content.append("evening")
        conditional_message_content.append("Have a great evening!")
    return conditional_message_content
