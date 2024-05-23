import firebase_admin
from firebase_admin import firestore, credentials

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
comments_ref = db.collection('comentarios')

def add_comment(data):    
    comments_ref.document(str(data['contact_email'])).set(data)