from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from .serializers import CustomerSerializer, CustomerCommentSerializer
from .models import Customer, Comment, Status, Headquarter
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    authentication_classes = (TokenAuthentication, )


class CustomerCommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerCommentSerializer
    queryset = Customer.objects.all()
    authentication_classes = (TokenAuthentication, )


def main(request):
    return HttpResponse('Hello')