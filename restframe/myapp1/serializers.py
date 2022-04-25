from asyncore import read
from dataclasses import field
from django.contrib.auth.models import User
from requests import request
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from myapp1.models import Category, Food, Order, Restaurants,Wishlist,Orderline,ProductReview


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)

    def create(self, validated_data):
        print("validated_data", validated_data)
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        print(user.password)
        user.save()
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('cat_name','image')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ('restorant_name', 'address')


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('name', 'description', 'price','image', 'category', 'restaurants')


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Wishlist
        fields = ('user', 'food')
        read_only_fields=['user']
    
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductReview
        fields = ('comment' ,'rating','foodId')
        read_only_fields=['user']


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('name','category', 'restaurants')

