from dataclasses import fields
from django.test import TestCase
from myapp1.models import Food, Restaurants, Category


class FoodModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        catg = Category.objects.create(cat_name="fastfood", image="myfood.png")
        restro = Restaurants.objects.create(
            restorant_name="shyamsandwitch", address="punjab")
        Food.objects.create(name="sandwitch", description="tasty", image="foodie.png", price="800",
                            category=catg, restaurants=restro)

    def test_name(self):
        field_label = Food._meta.get_field('name').max_length
        self.assertEqual(field_label, 50)

    def test_description(self):
        field_label = Food._meta.get_field('description').max_length
        self.assertEqual(field_label, 90)

    def test_price(self):
        field_label = Food._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'price')

    def test_image(self):
        field_label = Food._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')

    def test_category(self):
        field_label = Food._meta.get_field('category').verbose_name
        self.assertEqual(field_label, 'category')

    def test_restaurants(self):
        field_label = Food._meta.get_field('restaurants').verbose_name
        self.assertEqual(field_label, 'restaurants')


class RestaurantModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        Restaurants.objects.create(
            restorant_name="shyamsandwitch", address="delhi")

    def test_name(self):
        field_label = Restaurants._meta.get_field('restorant_name').max_length
        self.assertEqual(field_label, 70)

    def test_address(self):
        field_label = Restaurants._meta.get_field('address').max_length
        self.assertEqual(field_label, 80)
