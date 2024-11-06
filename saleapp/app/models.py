from saleapp.app import app, db
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Catigory(db.Model):
    id = Column(Integer, primary_key= True, autoincrement= True )
    name = Column(String(50), nullable=False)
    products = relationship('Product')

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column (Float, default=0)
    image = Column(String(100), nullable=True)
    active = Column(Boolean, default=True)
    catigory_id = Column(Integer, ForeignKey(Catigory.id), nullable=False)
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        c1 = Catigory(name = 'Moblie')
        c2 = Catigory(name = 'Desktop')
        c3 = Catigory(name = 'Tablet')

        db.session.add_all([c1,c2,c3])
        db.session.commit()