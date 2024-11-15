from flask import render_template, request
import dao
from app import app


@app.route("/")
def index():
    cate_id = request.args.get("category_id")
    cates = dao.load_categories()
    prods = dao.load_products(cate_id)
    return render_template('index.html', categories = cates, products = prods)


if __name__ == '__main__':
    app.run(debug=True)
