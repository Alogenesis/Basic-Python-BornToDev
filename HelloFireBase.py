import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('hellofirebase-11b78-firebase-adminsdk-pverj-98149195ec.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hellofirebase-11b78.firebaseio.com/'
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('AppName')
print(ref.get())

ref = db.reference('text')
print(ref.get())

ref = db.reference('textDemo')
print(ref.get())

ref = db.reference('Users/Sommai/Age')
print(ref.get())

ref = db.reference('Users/Sommai/Email')
print(ref.get())

ref = db.reference('Users/Sommai')
print(type(ref.get()))
print(ref.get())

hopper_ref = ref.child('Users/Sommai')
hopper_ref.delete()

ref = db.reference('Users')
print(type(ref.get()))
print(ref.get())