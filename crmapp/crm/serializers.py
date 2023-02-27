from rest_framework import serializers
from .models import Customer, Comment, User, Location


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username']


class CustomerSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(many=False)

    class Meta:
        model = Customer
        fields = ['id', 'name', 'tin', 'created_by']


class LocationSerializer(serializers.ModelSerializer):
    customer_id = CustomerSerializer(many=False, read_only=True)

    class Meta:
        model = Location
        fields = ['customer_id', 'city', 'street', 'apt_number', 'is_hq']


class CustomerLocationSerializer(serializers.ModelSerializer):
    location_id = LocationSerializer(many=True)

    class Meta:
        model = Customer
        fields = ['name', 'tin', 'created_by', 'location_id']


class CommentSerializer(serializers.ModelSerializer):
    location_id = LocationSerializer()

    class Meta:
        model = Comment
        fields = ['content', 'location_id']


class CustomerMainInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['name', 'tin', 'customer_id']
