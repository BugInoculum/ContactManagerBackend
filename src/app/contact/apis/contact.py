from flask import Blueprint, jsonify
from flask_restplus import Api, Resource, fields
from flask_cors import cross_origin
import logging

contacts_api = Blueprint('contacts_api', __name__)
api = Api(contacts_api)


contact_model = api.model('Contact', {
    'id': fields.String(required=True, description='Contact ID'),
    'firstName': fields.String(required=True, description='First Name'),
    'lastName': fields.String(required=True, description='Last Name'),
    'role': fields.String(required=True, description='Role'),
    'emailAddresses': fields.List(fields.String, description='Email Addresses'),
    'bio': fields.String(required=True, description='Bio'),
    'dial': fields.String(required=True, description='Dial-in Number'),
    'meeting': fields.String(required=True, description='Meeting Link'),
    'phoneNumbers': fields.List(fields.String, description='Phone Numbers'),
    'social': fields.Nested(api.model('Socials', {
        'linkedIn': fields.String(required=True, description='LinkedIn Profile URL'),
        'gmail': fields.String(required=True, description='Gmail Address'),
        'twitter': fields.String(required=True, description='Twitter Profile URL'),
        'faceBook': fields.String(required=True, description='Facebook Profile URL'),
    }), description='Social Media Links')
})

@api.route('/contacts')
class ContactList(Resource):
    @api.doc('list_contacts')
    def get(self):
        return contacts


@api.route('/contacts/<int:ID>/email_addresses')
class ContactEmailList(Resource):
    @api.doc('get_contact_emails')
    def get(self, ID):
       user = None
       logging.info(" id i got is: ", ID)
       print("id is", ID)
       contact = next((contact for contact in contacts if contact['id'] == ID), None)

       if contact:
           return contact
       else:
           print("id is", ID)
           return {'message': 'Contact not found'}, 404





# In-memory database
contacts = [
    {
        "id": 1,
        "firstName": "John",
        "lastName": "Doe",
        "role": "Software Engineer",
        "emailAddresses": ["john.doe@example.com"],
        "bio": "A passionate developer with a knack for solving complex problems.",
        "dial": "+1-234-567-8901",
        "meeting": "john.doe@calendly.com",
        "phoneNumbers": ["123-456-7890", "987-654-3210"],
        "social": {
            "linkedIn": "https://www.linkedin.com/in/johndoe",
            "gmail": "john.doe@gmail.com",
            "twitter": "https://twitter.com/johndoe",
            "faceBook": "https://facebook.com/johndoe"
        }
    },
    {
        "id": 2,
        "firstName": "Jane",
        "lastName": "Smith",
        "role": "Project Manager",
        "emailAddresses": ["jane.smith@example.com"],
        "bio": "Experienced project manager with a strong background in Agile methodologies.",
        "dial": "+1-234-567-8902",
        "meeting": "jane.smith@calendly.com",
        "phoneNumbers": ["234-567-8901", "876-543-2109"],
        "social": {
            "linkedIn": "https://www.linkedin.com/in/janesmith",
            "gmail": "jane.smith@gmail.com",
            "twitter": "https://twitter.com/janesmith",
            "faceBook": "https://facebook.com/janesmith"
        }
    },
    {
        "id": 3,
        "firstName": "Emily",
        "lastName": "Johnson",
        "role": "UX Designer",
        "emailAddresses": ["emily.johnson@example.com"],
        "bio": "Creative UX designer focused on delivering user-friendly solutions.",
        "dial": "+1-234-567-8903",
        "meeting": "emily.johnson@calendly.com",
        "phoneNumbers": ["345-678-9012", "765-432-1098"],
        "social": {
            "linkedIn": "https://www.linkedin.com/in/emilyjohnson",
            "gmail": "emily.johnson@gmail.com",
            "twitter": "https://twitter.com/emilyjohnson",
            "faceBook": "https://facebook.com/emilyjohnson"
        }
    },
    {
        "id": 4,
        "firstName": "Michael",
        "lastName": "Brown",
        "role": "Data Scientist",
        "emailAddresses": ["michael.brown@example.com"],
        "bio": "Data scientist with expertise in machine learning and big data.",
        "dial": "+1-234-567-8904",
        "meeting": "michael.brown@calendly.com",
        "phoneNumbers": ["456-789-0123", "654-321-0987"],
        "social": {
            "linkedIn": "https://www.linkedin.com/in/michaelbrown",
            "gmail": "michael.brown@gmail.com",
            "twitter": "https://twitter.com/michaelbrown",
            "faceBook": "https://facebook.com/michaelbrown"
        }
    },
    {
        "id": 5,
        "firstName": "Sarah",
        "lastName": "Davis",
        "role": "Marketing Specialist",
        "emailAddresses": ["sarah.davis@example.com"],
        "bio": "Innovative marketing specialist with a focus on digital strategies.",
        "dial": "+1-234-567-8905",
        "meeting": "sarah.davis@calendly.com",
        "phoneNumbers": ["567-890-1234", "543-210-9876"],
        "social": {
            "linkedIn": "https://www.linkedin.com/in/sarahdavis",
            "gmail": "sarah.davis@gmail.com",
            "twitter": "https://twitter.com/sarahdavis",
            "faceBook": "https://facebook.com/sarahdavis"
        }
    },
    {
        "id": 6,
        "firstName": "Chris",
        "lastName": "Martin",
        "role": "Content Writer",
        "emailAddresses": ["chris.martin@example.com"],
        "bio": "Skilled writer with a passion for creating compelling content.",
        "dial": "+1-234-567-8906",
        "meeting": "chris.martin@calendly.com",
        "phoneNumbers": ["678-901-2345", "432-109-8765"],
        "social": {
            "linkedIn": "https://www.linkedin.com/in/chrismartin",
            "gmail": "chris.martin@gmail.com",
            "twitter": "https://twitter.com/chrismartin",
            "faceBook": "https://facebook.com/chrismartin"
        }
    },
    {
        "id": 7,
        "firstName": "Olivia",
        "lastName": "Taylor",
        "role": "Graphic Designer",
        "emailAddresses": ["olivia.taylor@example.com"],
        "bio": "Passionate graphic designer creating visuals that communicate ideas.",
        "dial": "+1-234-567-8907",
        "meeting": "olivia.taylor@calendly.com",
        "phoneNumbers": ["789-012-3456", "321-098-7654"],
        "social": {
            "linkedIn": "https://www.linkedin.com/in/oliviataylor",
            "gmail": "olivia.taylor@gmail.com",
            "twitter": "https://twitter.com/oliviataylor",
            "faceBook": "https://facebook.com/oliviataylor"
        }
    },
    {
        "id": 8,
        "firstName": "David",
        "lastName": "Garcia",
        "role": "Network Administrator",
        "emailAddresses": ["david.garcia@example.com"],
        "bio": "Dedicated network administrator with a strong focus on cybersecurity.",
        "dial": "+1-234-567-8908",
        "meeting": "david.garcia@calendly.com",
        "phoneNumbers": ["890-123-4567", "210-987-6543"],
        "social": {
            "linkedIn": "https://www.linkedin.com/in/davidgarcia",
            "gmail": "david.garcia@gmail.com",
            "twitter": "https://twitter.com/davidgarcia",
            "faceBook": "https://facebook.com/davidgarcia"
        }
    },
    {
        "id": 9,
        "firstName": "Sophia",
        "lastName": "Lee",
        "role": "Product Owner",
        "emailAddresses": ["sophia.lee@example.com"],
        "bio": "Experienced product owner bridging the gap between development and business.",
        "dial": "+1-234-567-8909",
        "meeting": "sophia.lee@calendly.com",
        "phoneNumbers": ["901-234-5678", "109-876-5432"],
        "social": {
            "linkedIn": "https://www.linkedin.com/in/sophialee",
            "gmail": "sophia.lee@gmail.com",
            "twitter": "https://twitter.com/sophialee",
            "faceBook": "https://facebook.com/sophialee"
        }
    },
    {
        "id": 10,
        "firstName": "James",
        "lastName": "Wilson",
        "role": "DevOps Engineer",
        "emailAddresses": ["james.wilson@example.com"],
        "bio": "DevOps engineer with a passion for automation and continuous delivery.",
        "dial": "+1-234-567-8910",
        "meeting": "james.wilson@calendly.com",
        "phoneNumbers": ["012-345-6789", "098-765-4321"],
        "social": {
            "linkedIn": "https://www.linkedin.com/in/jameswilson",
            "gmail": "james.wilson@gmail.com",
            "twitter": "https://twitter.com/jameswilson",
            "faceBook": "https://facebook.com/jameswilson"
        }
    }
]