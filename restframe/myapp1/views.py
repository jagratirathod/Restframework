from django.contrib.sites.shortcuts import get_current_site
import datetime
from restframe import settings
import razorpay
from cart.cart import Cart
from django. db. models import Q
from myapp1.models import Category, Restaurants, Food, Order, Wishlist, Orderline, ProductReview
from urllib import response
from django.http import QueryDict
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import MyTokenObtainPairSerializer
from myapp1 import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from calendar import c
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import viewsets
from.serializers import UserSerializer, CategorySerializer, RestaurantSerializer, FoodSerializer, ReviewSerializer, WishlistSerializer,SearchSerializer
razorpay_client = razorpay.Client(
auth=(settings.razorpay_id, settings.razorpay_account_id))
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.


class Register(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'user_id': user.pk,
                    'email': user.email
                })
            return Response(serializer.data)
        else:
            return Response("User Already Exists")


class MyObtainTokenPairView(TokenObtainPairView,generics.GenericAPIView):       
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class mylogin(generics.GenericAPIView):
    parser_classes = (MultiPartParser, JSONParser)

    def post(self, request):
        email = request.data['email']
        user = User.objects.get(email=email)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            })

        else:
            return Response("Invalid user")


class Categorys(generics.GenericAPIView):
    serializer_class = CategorySerializer

    def get(self, request):
        query = Category.objects.all()
        serializer = CategorySerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Invalid")

class Category_update(generics.GenericAPIView):
    serializer_class = CategorySerializer
    
    def put(self, request, pk):
        query = Category.objects.get(id=pk)
        serializer = CategorySerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Updated data')
        else:
            return Response("Invalid")

    def delete(self, request, pk):
        query = Category.objects.get(id=pk)
        query.delete()
        return Response("Delete Successfully")


class Restaurant(generics.GenericAPIView):
    serializer_class = RestaurantSerializer

    def get(self, request):
        query = Restaurants.objects.all()
        serializer = RestaurantSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Inavlid")

class Restaurant_update(generics.GenericAPIView):
    serializer_class = RestaurantSerializer
    def put(self, request, pk):
        query = Restaurants.objects.get(id=pk)
        serializer = RestaurantSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Successfully Updated data')
        else:
            return Response("INVALID")


    def delete(self, request, pk):
        query = Restaurants.objects.get(id=pk)
        query.delete()
        return Response("Delete Successfully")


class Foods(generics.GenericAPIView):
    # authentication_classes=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    serializer_class = FoodSerializer

    def get(self, request):
        query = Food.objects.all()
        serializer = FoodSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("Invalid Data")


class MyWishlist(generics.GenericAPIView):
    serializer_class = WishlistSerializer

    def get(self, request):
        query = Wishlist.objects.all()
        serializer = WishlistSerializer(query, many=True)
        return Response(serializer.data)

class AddInWishlist(generics.GenericAPIView):
    serializer_class = WishlistSerializer

    
    def post(self,request,pk):
        # import pdb; pdb.set_trace()
        food = Food.objects.get(id=pk)
        food_in_wish = Wishlist.objects.filter(
                    Q(food=food) & Q(user=request.user)).exists()

        if food_in_wish == False:
            wishlist = Wishlist.objects.create(user=request.user, food=food)
            serializer = WishlistSerializer(wishlist)
            return Response(serializer.data)
        else:
            return Response({'status': 200, "msg": "Food Already Exists"})

    
    def delete(self, request, pk):
        query = Wishlist.objects.get(id=pk)
        query.delete()
        return Response("Delete Successfully")


class ReviewProduct(generics.GenericAPIView):
    serializer_class = ReviewSerializer
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        else:
            return Response("invalid dta")


class cart_add(generics.GenericAPIView):
    def get(self, request, pk):
        cart = Cart(request)
        product = Food.objects.get(id=pk)
        cart.add(product=product)
        return Response("Successfully Add to Cart")


class Payment(APIView):

    def post(self, request):
        cart = Cart(request)
        user = self.request.user
        order = Order.objects.create(
            user=request.user, order_date=datetime.datetime.now(), totalprice=0)
        final_price = 0

        for value in cart.cart.values():
            price = int(value.get('price'))
            quantity = int(value.get('quantity'))
            food = int(value.get('product_id'))
            final_price = final_price + (price*quantity)
            orderline = Orderline.objects.create(
                order=order, totalquantity=quantity, food_id=food)
        order.totalprice = final_price
        callback_url = 'http://' + \
            str(get_current_site(request))+"/customer/handlerequest/"
        razorpay_order = razorpay_client.order.create(dict(
            amount=final_price*100, currency=settings.order_currency, payment_capture='0'))
        print(razorpay_order['id'])
        order.order_id = razorpay_order['id']
        order.save()
        orderline = Orderline.objects.filter(order=order)
        cart.clear()
        return Response("Successfully Payment done")


class SearchView(generics.GenericAPIView):
    def get(self, request):
        query = self.request.GET.get('q')
        foods = Food.objects.all()
        if query:
            foods = foods.filter(Q(name__icontains=query) | Q(
                restaurants__restorant_name__icontains=query) | Q(category__cat_name__icontains=query))
        serializer = SearchSerializer(foods, many=True)
        print("padsd",foods)
        return Response(serializer.data)


class Filterby(generics.GenericAPIView):
    def get(self, request, sort=None):
        # import pdb; pdb.set_trace()
        if sort == "LTH":
            filter1 = Food.objects.all().order_by('price')
        else:
            filter1 = Food.objects.all().order_by('-price')

        serializer = FoodSerializer(filter1, many=True)
        return Response(serializer.data)
