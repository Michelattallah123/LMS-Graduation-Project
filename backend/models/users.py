from backend.models.config import db
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(db.Model,Base):
 __tablename__ = 'user'
 user_id        =  db.Column(db.Integer, primary_key=True)
 name           =  db.Column(db.String(50),nullable=False)
 email          =  db.Column(db.String(50),nullable=False)
 national_id    =  db.Column(db.Integer,nullable=False, unique=True)
 birthday       =  db.Column(db.Date,nullable=False)
 password       =  db.Column(db.String(255))

 '''
 Relations
 '''
 student            =  relationship("Student", back_populates="user", passive_deletes=True)
 professor          =  relationship("Professor", back_populates="user", passive_deletes=True)


 def serialize(self):
        return {
            'id': self.user_id,
            'name': self.name
        }

 def get(self,user_id):
     user = self.query.filter_by(user_id=user_id).one()
     return user.serialize()