    
from mongoalchemy.session import Session

def get_mongo_session():
    return Session.connect("mongodb://localhost:27017/saap_src_data")