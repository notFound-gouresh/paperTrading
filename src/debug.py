import firebase_admin
from firebase_admin import credentials
from credentials import __cred__

cred = credentials.Certificate(__cred__)
firebase_admin.initialize_app(cred)
