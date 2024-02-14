import factory
import fake
from factory.django import DjangoModelFactory
from faker import Faker

from products.models import Product, Category, Tag


# fake = Faker(locale='uk_UA')

class CategoryFactory(DjangoModelFactory):
    name = factory.Faker('word')

    class Meta:
        model = Category

class TagFactory(DjangoModelFactory):
    name = factory.Faker('word')

    class Meta:
        model = Tag


class ProductFactory(DjangoModelFactory):
    tittle = factory.Faker('word')
    description = factory.Faker('sentence')
    price = factory.Faker('pyfloat', left_digits=4, right_digits=2, positive=True)
    summary = factory.Faker('sentence')
    is_18_plus = factory.Faker('pybool')
    featured = factory.Faker('pybool')

    class Meta:
        model = Product


