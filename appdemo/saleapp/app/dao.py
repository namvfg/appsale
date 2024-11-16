from itertools import product

from app.models import Category, Product
from app import db, app

def load_categories():
    return Category.query.order_by("id").all()


def load_products(cate_id=None, page=1):
    query = Product.query

    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))
    page_size = app.config["PAGE_SIZE"]
    start = (page - 1) * page_size
    query = query.slice(start, start + page_size)

    return query.all()

def count_products():
    return Product.query.count()


