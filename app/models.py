from sqlalchemy.orm import relationship
from flask_login import UserMixin
from app import db

from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
class Category(db.Model):
    __tablename__='category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name= Column(String(50),nullable=False, unique=True)
    products=relationship('Product', backref='category',lazy=True)
    def __str__(self):
        return self.name


class Product(db.Model):

    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(200))
    category_id = Column(Integer , ForeignKey(Category.id), nullable=False)

class User(db.Model, UserMixin):
__tablename__ = 'user'
id = Column(Integer, primary_key=True,
autoincrement=True)
name = Column(String(50), nullable=False)
active = Column(Boolean, default=True)
username = Column(String(50), nullable=False)
password = Column(String(100), nullable=False)
avatar =Column(String(100), default="https://shoppingaz.vn/wp-content/uploads/2022/03/loa-bluetooth-harman-kardon-onyx-studio-5.jpg")
if __name__=='__main__':
    from app import app
    with app.app_context():
        # c1=Category(name='Mobile')
        # c2=Category(name='Tablet')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.commit()
        import hashlib
        u =User(name='Admin', username='admin', password=str(hashlib.md5()) )

        p1 = Product(name='Iphone 15', price=30000, category_id=1, image= "https://tcct.aicmscdn.net/tcct-media/23/9/12/iphone-15-pro-max_64ffced304ab9.png" )
        p2 = Product(name='Tablet', price=30000, category_id=2, image="https://p2-ofp.static.pub/ShareResource/na/subseries/hero/lenovo-slim-7i-14inch.png")
        p3 = Product(name='Laptop', price=30000, category_id=1, image="https://p2-ofp.static.pub/fes/cms/2023/02/22/pkhjbh23c7sjfxf76k6e6usevy3ixi851221.png")
        p4 = Product(name='Loa', price=30000, category_id=2, image="https://shoppingaz.vn/wp-content/uploads/2022/03/loa-bluetooth-harman-kardon-onyx-studio-5.jpg")

        db.session.add_all([p1,p2,p3,p4])
        db.session.commit()

      # db.create_all()


