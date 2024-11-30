import math

from flask import render_template, request, redirect
from flask_login import login_user, logout_user
from app.models import UserRole
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

@app.route("/logout")
def logout_my_user():
    logout_user()
    return redirect("/")

@app.route("/login-admin", methods=["post"])
def admin_login():
    username = request.form['username']
    password = request.form['password']

    user = dao.auth_user(username=username, password=password)
    if user: #and user["user_role"].__eq__(UserRole.ADMIN)
        login_user(user)
    return redirect("/admin")



@login.user_loader
def load_user(userid):
    return dao.get_user_by_id(userid)


if __name__ == '__main__':
    from app import admin
    app.run(debug=True)
