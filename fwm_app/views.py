from django.shortcuts import render
from rest_framework import viewsets

from .serializers import *

class AddressAPI(viewsets.ModelViewSet):
	serializer_class = AddressSerializer
	queryset = Address.objects.all()

class VendorAPI(viewsets.ModelViewSet):
	serializer_class = VendorSerializer
	queryset = Vendor.objects.all()

class OrganizationAPI(viewsets.ModelViewSet):
	serializer_class = OrganizationSerializer
	queryset = Organization.objects.all()

class CustomerAPI(viewsets.ModelViewSet):
	serializer_class= CustomerSerializer
	queryset = Customer.objects.all()

class OrdersAPI(viewsets.ModelViewSet):
	serializer_class= OrdersSerializer
	queryset = Orders.objects.all()

class ProductAPI(viewsets.ModelViewSet):
	serializer_class=ProductSerializer
	queryset = Products.objects.all()
