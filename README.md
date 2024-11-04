# Contact Manager Backend

This is a simple backend application for managing contacts built with Flask and Flask-RestPlus. It provides a RESTful API to handle contact information, including personal details and social media links.

## Features

- **List Contacts**: Retrieve a list of all contacts.
- **Get Contact Emails**: Retrieve email addresses for a specific contact by ID.
- **In-memory Database**: Contact data is stored in memory for demonstration purposes.

## Technologies Used

- **Python**: Version 3.x
- **Flask**: Web framework for building the API
- **Flask-RestPlus**: Extension for building REST APIs
- **Flask-CORS**: For handling Cross-Origin Resource Sharing
- **Logging**: For logging application activity

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/BugInoculum/ContactManagerBackend.git
   cd ContactManagerBackend

 pip install virtualenv
 virtualenv venv  # Create a virtual environment named venv
 source venv/bin/activate  # On Windows use `venv\Scripts\activate`
 pip install -r requirements.txt
 python src/main.py  
