import firebase_admin
from firebase_admin import credentials
from pyrebase import initialize_app

# Initialize Firebase using firebase_admin
cred = credentials.Certificate("database/credentials.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "firebase-database-url",
    "storageBucket": "storage-bucket-id"
})

# Initialize Firebase using pyrebase
firebaseConfig = {
    "add credentials here"
}

auth = initialize_app(firebaseConfig).auth()