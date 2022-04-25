from unicodedata import category
from urllib import response
from myapp1.test.tests_setup import TestSetUp, TestSetUp1, TestSetUp2, TestSetup3
import json
from ..models import User, Category, Restaurants, Food
from django.urls import reverse
import json
import base64


class UserRegister(TestSetUp):
    # def test_user_cannot_register_with_no_data(self):
    #     # import pdb; pdb.set_trace()
    #     res = self.client.post(self.register_url)
    #     self.assertEqual(res.status_code, 200)

    def test_register_post(self):
        res = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(res.data['email'], self.user_data['email'])
        self.assertEqual(res.status_code, 200)

    # def test_user_cannot_login_with_unverified_email(self):
    #     self.client.post(
    #         self.register_url, self.user_data, format="json")
    #     res = self.client.post(self.login_url, self.user_data, format="json")
    #     self.assertEqual(res.status_code, 401)

    def test_login_post(self):
        response = self.client.post(
            self.register_url, self.user_data, format="json")
        email = response.data['email']
        user = User.objects.get(email=email)
        user.is_verified = True
        user.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 200)


class AddCategory(TestSetUp1):
    def test_category_get(self):
        cat = Category(cat_name="indianfood", image="hello.png")
        cat.save()
        res = self.client.get(self.category_url, format="json")
        # print("response", res.data)
        self.assertEqual(res.status_code, 200)

    # def test_category_post(self):
    #     res = self.client.post(
    #         self.category_url, self.catg_data, format="json")
    #     print("helloworld :", res.data)
    #     self.assertEqual(res.status_code, 200)


class AddRestaurant(TestSetUp2):
    def test_restaurant_get(self):
        resto = Restaurants(
            restorant_name="rangella dhaba", address="delhi")
        resto.save()
        res = self.client.get(self.restaurant_url, format="json")
        # print("lkdsjkldsklfklsfjkl", res.data)
        self.assertEqual(res.status_code, 200)

    def test_restaurant_post(self):
        res = self.client.post(
            self.restaurant_url, self.restaurant_data, format="json")
        # print(res.data)
        self.assertEqual(res.status_code, 200)

    def test_restaurant_put(self):
        myrest = Restaurants(restorant_name="shamsandwitch", address="punjab")
        myrest.save()

        self.myrestaurant_url = reverse(
            'myrestaurant', kwargs={'pk': myrest.pk})
        res = self.client.put(self.myrestaurant_url,
                              self.restaurant_data, format="json")
        # print("helloworld : ", res.data)
        self.assertEqual(res.status_code, 200)

    def test_restaurant_delete(self):
        # myrest = Restaurants(restorant_name="shamsandwitch", address="punjab")
        # myrest.save()

        myrest = Restaurants.objects.create(restorant_name="shamsandwitch", address="punjab")
        self.myrestaurant_url = reverse('myrestaurant', kwargs={'pk': myrest.pk})
        res = self.client.delete(self.myrestaurant_url, format="json")
        self.assertEqual(res.status_code, 200)

        # self.assertEqual(Restaurants.objects.count(), 1)
        # print(Restaurants.objects.count())


class Addfood(TestSetup3):
    def test_food_get(self):
        category = Category.objects.create(cat_name="Indianfood", image="food.png")
        restaurant = Restaurants.objects.create(restorant_name="rangella dhaba", address="bhopal")

        resto = Food.objects.create(name="maggi", description="tasty", price="522",image="smile.png", category=category, restaurants=restaurant)
        res = self.client.get(self.foods_url)
        # print("hii its sunny :", res.data)
        self.assertEqual(res.status_code, 200)

    def test_food_post(self):
        res = self.client.post(
            self.foods_url,data=self.foodie_data, files=self.image_data,format="json")
        # print(res.data)
        self.assertEqual(res.status_code, 200)
