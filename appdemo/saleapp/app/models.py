from app import db, app
from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Category(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True)

    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    image = Column(String(100), nullable=True)
    price = Column(Float, default=0)
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # c1 = Category(name="Mobile")
        # c2 = Category(name="Tablet")
        # c3 = Category(name="Laptop")
        # db.session.add_all([c1, c2, c3])
        # db.session.commit()