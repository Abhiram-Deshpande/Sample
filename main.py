import firebase_admin
from firebase_admin import credentials, db, storage
import firebase_admin.storage
import firebase_config
import os

cred = credentials.Certificate("bookstoreproject-a6dc0-firebase-adminsdk-a5n3g-7e0d1b9312.json")
firebase_admin.initialize_app(cred,firebase_config.firebaseConfig)

bucket = storage.bucket()
blob_list = bucket.list_blobs()
# print(firebase_admin.get_app().name)

image = bucket.blob(blob_name="/blurred_images/football.png")
print(image.size)

# ref = db.reference("")
# users_ref = ref.child('users')
# users_ref.set({
#     'alanisawesome': {
#         'date_of_birth': 'June 23, 1912',
#         'full_name': 'Alan Turing'
#     },
#     'gracehop': {
#         'date_of_birth': 'December 9, 1906',
#         'full_name': 'Grace Hopper'
#     }
# })
