# create_db.py

from flask_sqlalchemy import SQLAlchemy
from database import db, app

# Your database creation code here

class User(db.Model):
    __tablename__ = 'user'  # Ensure that the table name matches the existing table
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(100))
    cash_in_hand = db.Column(db.Integer, default=500)
    stock = db.relationship('Stock', backref='owner')

class Stock(db.Model):
    __tablename__ = 'stock'  # Ensure that the table name matches the existing table
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    qty = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.Integer)

class Transaction(db.Model):
    __tablename__ = 'transaction'  # Ensure that the table name matches the existing table
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))
    name = db.Column(db.String(50))
    qty = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    create_tables()
