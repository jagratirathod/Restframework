from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import User, Category, Restaurants, Food
from PIL import Image
import io
from django.core.files.base import ContentFile
from io import StringIO
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile


def create_image(storage, filename, size=(100, 100), image_mode='RGB', image_format='PNG'):
    """
    Generate a test image, returning the filename that it was saved as.

    If ``storage`` is ``None``, the BytesIO containing the image data
    will be passed instead.
    """
    data = io.BytesIO()
    Image.new(image_mode, size).save(data, image_format)
    data.seek(0)
    if not storage:
        return data
    image_file = ContentFile(data.read())
    return storage.save(filename,image_file)


# from faker import Faker

# Create your tests here.


class TestSetUp(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        # self.fake = Faker()

        self.user_data = {
            'email': 'jagrati02@gmail.com',
            'username': 'jagrati',
            'password': 'jagrati@123',
            "first_name": "jagrati",
            "last_name": "rathod"
        }
        return super().setUp()


class TestSetUp1(APITestCase):
    def setUp(self):
        self.category_url = reverse('category')

        fake = create_image(None, 'fake.png')
        avatar_file = SimpleUploadedFile('front.png', fake.getvalue())

        self.catg_data = {
            'cat_name': 'chinese',
            'image': avatar_file
        }
        return super().setUp()


class TestSetUp2(APITestCase):
    def setUp(self):
        self.restaurant_url = reverse('restaurant')

        self.restaurant_data = {
            'restorant_name': 'shyamsandich',
            'address': 'indore'

        }
        return super().setUp()

import io

class TestSetup3(APITestCase):
    def setUp(self):
        self.foods_url = reverse('foods')

        restorat = Restaurants.objects.create(restorant_name="rangeela bhaba", address="agra")
        print("restorat", restorat)

        category = Category.objects.create(cat_name="Itallian", image="ghg.png")
        print("category", category)

        myimage = create_image(None, 'fake.png')
        avatar_file = SimpleUploadedFile('front.png', myimage.getvalue())
        
        self.foodie_data = {
            "name": "noodles",
            "description": "yummy",
            "price": "100",
            "restaurants": restorat.pk,
            "category": category.pk,
        }

        self.image_data={"image": avatar_file}
        return super().setUp()

    def tearDown(self):
        return super().tearDown()
