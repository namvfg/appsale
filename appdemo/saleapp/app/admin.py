from flask_admin import Admin, BaseView, expose
from app.models import Product, Category, User
from flask_admin.contrib.sqla import ModelView
from app import db
from app import app
from flask import render_template, redirect

class CategoryView(ModelView):
    column_list = ["name", "products"]


class ProductView(ModelView):
    column_list = ["id", "name", "description", "price", "active"]
    column_searchable_list = ["name", "description"]
    column_filters = ["name", "price"]
    can_export = True

# class LogoutView(BaseView):
#     @expose("/")
#     def index(self):
#

class StatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin/stats.html")

admin = Admin(app=app, name="Quản trị bán hàng", template_mode="bootstrap4")
admin.add_view(CategoryView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
admin.add_view(ModelView(User, db.session))

admin.add_view(StatsView(name="Thống kê"))