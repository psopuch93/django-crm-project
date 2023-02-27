from django.core.exceptions import MultipleObjectsReturned
from django.utils.datastructures import MultiValueDictKeyError
from django.db import IntegrityError
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CustomerSerializer, LocationSerializer, CustomerMainInfoSerializer,\
    CustomerLocationSerializer, CommentSerializer
from .models import Customer, Comment, Status, Location
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication, )
    queryset = Customer.objects.all()

    def create(self, request, *args, **kwargs):
        customer_data = request.data
        user = request.user
        try:
            new_customer = Customer.objects.create(name=customer_data["name"], tin=customer_data["tin"], created_by=user)
            new_customer.save()
            serializer = CustomerSerializer(new_customer)
        except IntegrityError:
            return HttpResponse('Exception: Duplicated unique value')
        return Response(serializer.data)

    def list(self, request):
        serializer_class = CustomerSerializer(self.queryset, many=True)
        response = serializer_class.data
        return Response(response, status=status.HTTP_200_OK)


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