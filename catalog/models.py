from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    picture = Column(String(255), nullable=True)
    name = Column(String(80), nullable=False)
    email = Column(String(255), nullable=False)
    email_verified = Column(String(255), nullable=False)

    def __str__(self):
        return 'User: {}'.format(self.name)


class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    def __str__(self):
        return 'Category: {}'.format(self.name)


class Item(Base):

    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True, default=None)
    created_by = Column(String(255), nullable=False)
    name = Column(String(80), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    condition = Column(String(4), nullable=False)
    production_year = Column(String(50), nullable=True)
    price = Column(String(50), nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'category': self.category_id,
            'condition': self.condition,
            'production_year': self.production_year
        }

    def to_dict(self):
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            category=self.category_id,
            condition=self.conditiion,
            production_year=self.production_year
        )

    def is_owner(self, user=None):
        if user is not None:
            return True if self.created_by == user['id'] else False
        else:
            raise Exception



    def __str__(self):
        return self.name
