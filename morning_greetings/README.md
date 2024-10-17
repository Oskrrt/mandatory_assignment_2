# mandatory_assignment_2

Python code for the second mandatory assignment for subject "problem-solving with scripting"

## Table of Contents

- [Important](#important)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Things I did not have time for](#future-work)

## Important

- The structure and some of the content of this readme file are copied from the readme in
  **ACIT_GAME_MODULE** example.
- ***setup.py*** and ***pyproject.toml*** is also taken from ACIT_GAME_MODULE. Edited setup.py according to this
  package.

## Features

- Generate greeting message based on the recipient and the time of day
- Sending messages
- Logging of events: message sending, message generation
- Contact list management: add, remove, get, print

## Installation

To get started, follow these steps:

1. **Clone the Repository** (or download the files):
   ```bash
   git clone https://github.com/Oskrrt/mandatory_assignment_2.git
   ```
2. **Navigate to the Project Directory**:
   ```bash
   cd mandatory_assignment_2
   ```
3. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**:
    - On **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - On **Mac/Linux**:
      ```bash
      source venv/bin/activate
      ```

## Usage

## Future work

***Things I planned on doing but did not have time for:***

- Unit testing.
- More in depth error handling with logging of error messages to file.
- Regex validation on name, email and preferred_time, especially when adding contacts.
- Some form of user interface popup for contact management
- 