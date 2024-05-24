from rest_framework import serializers
from .models import *

class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model=Address
		fields="__all__"

class VendorSerializer(serializers.ModelSerializer):
	class Meta:
		model=Vendor
		fields="__all__"

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model=Customer
		fields="__all__"

class OrganizationSerializer(serializers.ModelSerializer):
	class Meta:
		model=Organization
		fields="__all__"

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model=Products
		fields="__all__"

class OrdersSerializer(serializers.ModelSerializer):
	class Meta:
		model=Orders
		fields="__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['account_email', 'account_password']
		
