
from rest_framework import serializers
from .models import *

class StaffSerilalizer(serializers.ModelSerializer):

    class Meta:

        model = Staff
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):

    class Meta:

        model = Car
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer
        fields = '__all__'


class RentalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rental
        fields = '__all__'
