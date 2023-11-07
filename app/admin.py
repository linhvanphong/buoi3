from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app import app, db
from app.models import Category,Product
class MyProductView(ModelView):
    column_list = ['id', 'name', 'price','category_id']
    column_searchable_list = ['name']
    column_filters = ['price', 'name']
    column_editable_list = ['name']
    can_export = True

class MyCategoryView(ModelView):

    column_list = ['name', 'product']
class MyStaticView(BaseView):
    @expose("/")
    def __index__(self):
        return self.render('admin/stats.html')
admin = Admin(app, name="Quan ly ban hang", template_mode="bootstrap3")


admin.add_view(MyCategoryView(Category,db.session))
#admin.add_view(MyProductView(Product,db.session))

admin.add_view(MyStaticView(name='Thống khổ bảo kê'))


