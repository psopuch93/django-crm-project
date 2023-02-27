from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from .serializers import CustomerSerializer, LocationSerializer, CustomerMainInfoSerializer,\
    CustomerLocationSerializer, CommentSerializer
from .models import Customer, Comment, Status, Location
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    authentication_classes = (TokenAuthentication, )


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    authentication_classes = (TokenAuthentication, )


class CustomerMainInfoViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerLocationSerializer
    queryset = Customer.objects.all()
    authentication_classes = (TokenAuthentication, )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    authentication_classes = (TokenAuthentication, )


def main(request):
    return HttpResponse('Hello')