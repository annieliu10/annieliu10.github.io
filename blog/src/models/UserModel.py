from marshmallow import fields, Schema 
import datetime
from . import db 


## building the user model 
class UserModel(db.Model):

    ## table name of the model 
    __tablename__ = 'users'
    
    ## creating columns 
    id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique= True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    ##data will be a dictionary of data 
    def __init__(self, data):
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = data.get('password')
        self.created_at = data.get('created_at')
        self.modified_at = data.get('modified_at')

    ## save users to the db 
    def save(self):
        db.sessions.add(self)
        db.sessions.commit()

    






