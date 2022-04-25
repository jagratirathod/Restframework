from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=50, unique=True)
    image = models.ImageField(
        upload_to='category/media/', unique=True, default=None)

    def __str__(self):
        return f"{self.cat_name}"


class Restaurants(models.Model):
    restorant_name = models.CharField(max_length=70)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.restorant_name}"


class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=90)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    restaurants = models.ForeignKey(Restaurants, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
             ('Pending','Pending'),
             ('Done', 'Done'),
             ('Fail', 'Fail')
    )
    status = models.CharField(max_length=20, choices=STATUS, default="Pending")
    order_date = models.DateTimeField()
    totalprice = models.IntegerField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=60, default="")

    def __str__(self):
        return f"{self.id}"

class Orderline(models.Model):
    totalquantity = models.IntegerField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


    def __int__(self):
        return self.id

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)


class ProductReview(models.Model):
    RATING = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    foodId= models.ForeignKey(Food, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.CharField(choices=RATING, max_length=150)

    def __str__(self):
        return self.rating
