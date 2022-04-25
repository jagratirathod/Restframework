from django.shortcuts import render
from rest_framework import viewsets
from myapp1.models import Food
from myapp1.serializers import FoodSerializer
# from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly


# Create your views here.

class MyViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    # authentication_classes=[TokenAuthentication]
    # permission_classes=[IsAuthenticated]

    # session

    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]

    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticatedOrReadOnly]

    # authentication_classes=[SessionAuthentication]
    # permission_classes=[DjangoModelPermissions]

    # authentication_classes=[SessionAuthentication]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]

    #  authentication

    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]

    # authentication_classes=[BasicAuthentication]
    # permission_classes=[AllowAny]

    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAdminUser]
