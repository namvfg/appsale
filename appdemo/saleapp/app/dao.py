
from app.models import Category, Product, User
from app import app
import hashlib

def load_categories():
    return Category.query.order_by("id").all()


def load_products(cate_id=None, page=1, keyword=None):
    query = Product.query

    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))

    if keyword:
        query = query.filter(Product.name.contains(keyword))

    page_size = app.config["PAGE_SIZE"]
    start = (page - 1) * page_size
    query = query.slice(start, start + page_size)

    return query.all()

def count_products():
    return Product.query.count()

def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode("utf-8")).digest())
    return User.query.filter(User.username.__eq__(username.strip()), User.password.__eq__(password)).first()

def get_user_by_id(userid):
    return User.query.get(userid)


