from itertools import product

from app.models import Category, Product
from app import db, app

def load_categories():
    return Category.query.order_by("id").all()


def load_products(cate_id=None):
    query = Product.query

    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))

    return query.all()



