from email.policy import default

from flask_admin.contrib.geoa import ModelView
from flask_sqlalchemy.model import Model
from app import db, app
from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from enum import Enum as UserEnum
from flask_login import UserMixin
import hashlib

class UserRole(UserEnum):
    USER = 1
    ADMIN = 2

class BaseModel(db.Model):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)

class Category(BaseModel):
    name = Column(String(50), nullable=False)

    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    image = Column(String(100), nullable=True)
    price = Column(Float, default=0)
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

class User(BaseModel, UserMixin):
    name = Column(String(50), nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100))
    active = Column(Boolean, default=True)
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        u = User(name="Nguyễn Nam", username="namvfg",
                 password=str(hashlib.md5("123456".encode("utf-8")).digest()),
                 avatar="https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg")
        db.session.add(u)
        db.session.commit()

        # c1 = Category(name="Mobile")
        # c2 = Category(name="Tablet")
        # c3 = Category(name="Laptop")
        # db.session.add_all([c1, c2, c3])
        # products = [{
        #     "id": 1,
        #     "name": "iPhone 7 Plus",
        #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #     "price": 17000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 2,
        #     "name": "iPad Pro 2020",
        #     "description": "Apple, 128GB, RAM: 6GB",
        #     "price": 37000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        #     "category_id": 2
        # }, {
        #     "id": 3,
        #     "name": "Galaxy Note 10 Plus",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 4,
        #     "name": "iPhone 7 Plus",
        #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #     "price": 17000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 5,
        #     "name": "iPad Pro 2020",
        #     "description": "Apple, 128GB, RAM: 6GB",
        #     "price": 37000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        #     "category_id": 3
        # }, {
        #     "id": 6,
        #     "name": "Galaxy Note 10 Plus",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 7,
        #     "name": "iPhone 7 Plus",
        #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #     "price": 17000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        #     "category_id": 1
        # }, {
        #     "id": 8,
        #     "name": "iPad Pro 2020",
        #     "description": "Apple, 128GB, RAM: 6GB",
        #     "price": 37000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        #     "category_id": 2
        # }, {
        #     "id": 9,
        #     "name": "Galaxy Note 10 Plus",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #     "category_id": 3
        # }, {
        #     "id": 10,
        #     "name": "iPhone 7 Plus",
        #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
        #     "price": 17000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
        #     "category_id": 3
        # }, {
        #     "id": 11,
        #     "name": "iPad Pro 2020",
        #     "description": "Apple, 128GB, RAM: 6GB",
        #     "price": 37000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        #     "category_id": 2
        # }, {
        #     "id": 12,
        #     "name": "Galaxy Note 10 Plus",
        #     "description": "Samsung, 64GB, RAML: 6GB",
        #     "price": 24000000,
        #     "image":
        #         "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
        #     "category_id": 1
        # }]
        # for p in products:
        #     p = Product(**p)
        #     db.session.add(p)
        # db.session.commit()
