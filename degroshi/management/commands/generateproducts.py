import random

from django.core.management import BaseCommand

from products.management.commands.factories import ProductFactory, CategoryFactory, TagFactory
from products.models import Product

from faker import Faker

# fake = Faker(locale='uk_UA')


# genarate products
class Command(BaseCommand):
    def handle(self, *args, **options):
        tags = TagFactory.create_batch(1000)
        categories = CategoryFactory.create_batch(1000)

        products = ProductFactory.create_batch(1000)

        for product in products:
            randon_category = random.choice(categories)
            random_tags = random.sample(tags, random.randint(1, 10))

            product.category = randon_category
            product.tags.set(random_tags)

            product.save()


