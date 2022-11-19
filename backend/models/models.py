from sqlalchemy import Column, String, Integer, DateTime, Float
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""
def setup_db(app):
    db.app = app
    db.init_app(app)
    db.create_all()

"""
Transaction
"""
class Transaction(db.Model):
    __tablename__ = 'transaction'
    # Cols
    id = Column(String, primary_key=True)
    user_id = Column(String, db.ForeignKey('user.id'), nullable=True)
    category_id = Column(String, db.ForeignKey('category.id'), nullable=True)
    date = Column(DateTime(timezone=True))
    amount = Column(Float)
    currency = Column(String)

    def __init__(self, id, user_id, category_id, date, amount, currency):
        self.id = id
        self.user_id = user_id
        self.category_id = category_id
        self.date = date
        self.amount = amount
        self.currency = currency

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'date': self.date,
            'amount': self.amount,
            'currency': self.currency,
        }


"""
TransactionType
"""
class TransactionType(db.Model):
    __tablename__ = 'transaction_type'
    # Cols
    id = Column(String, primary_key=True)
    type = Column(String)
    # Rel
    categories = db.relationship('Category', backref='transaction_type', lazy=True)

    def __init__(self, id, type):
        self.id = id
        self.type = type

    def format(self):
        return {
            'id': self.id,
            'type': self.type
        }


"""
Category
"""
class Category(db.Model):
    __tablename__ = 'category'
    # Cols
    id = Column(String, primary_key=True)
    transaction_type_id = Column(String, db.ForeignKey('transaction_type.id'))
    type = Column(String)
    # Rel
    transactions = db.relationship('Transaction', backref='category', lazy=True)

    def __init__(self, id, transaction_type_id, type):
        self.id = id
        self.transaction_type_id = transaction_type_id
        self.type = type

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'transaction_type_id': self.transaction_type_id,
            'type': self.type
        }


"""
User
"""
class User(db.Model):
    __tablename__ = 'user'
    # Cols
    id = Column(String, primary_key=True)
    name = Column(String)
    # Rel
    transactions = db.relationship('Transaction', backref='user', lazy=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name
        }
