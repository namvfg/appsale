import math

from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    page = request.args.get("page")
    cate_id = request.args.get("category_id")
    cates = dao.load_categories()
    prods = dao.load_products(cate_id=cate_id, page=int(page))
    total = dao.count_products()
    page_size = app.config["PAGE_SIZE"]
    return render_template('index.html', categories = cates, products = prods, pages=math.ceil(total / page_size))


if __name__ == '__main__':
    app.run(debug=True)
