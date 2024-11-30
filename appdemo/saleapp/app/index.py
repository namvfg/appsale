import math

from flask import render_template, request, redirect
from flask_login import login_user

from app import dao
from app import app, login

@app.route("/")
def index():
    page = request.args.get("page", 1)
    cate_id = request.args.get("category_id")
    kw = request.args.get("keyword")

    cates = dao.load_categories()
    prods = dao.load_products(cate_id=cate_id, page=int(page), keyword=kw)
    total = dao.count_products()
    page_size = app.config["PAGE_SIZE"]

    return render_template('index.html',
                           categories = cates,
                           products = prods,
                           pages=math.ceil(total / page_size))

@app.route("/login", methods=['get', 'post'])
def login_my_user():
    if request.method.__eq__('POST'):
        username = request.form["username"]
        password = request.form["password"]
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            return redirect("/")
    return render_template("login.html")

@login.user_loader
def load_user(userid):
    return dao.get_user_by_id(userid)


if __name__ == '__main__':
    app.run(debug=True)
