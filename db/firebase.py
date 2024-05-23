import reflex as rx

import firebase_admin
from firebase_admin import firestore, credentials

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
comments_ref = db.collection('comentarios')

def add_comment(data):  
    doc_ref= comments_ref.add(data)
   
    response = search_comment(doc_ref)
    rx.console.log(response)
#    return response

   

def search_comment(id):
    doc = comments_ref.document(id).get()
    rx.console.log(doc)
    # doc_ref = db.collection("cities").document("SF")
    # doc = doc_ref.get()
    if doc.exists:
        return True
    else:
        return False

# def add_comment(data):    
#     comments_ref.document(str(data['contact_email'])).set(data)