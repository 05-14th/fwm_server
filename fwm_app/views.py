from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import Accounts
import json
from django.db import connection



from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response


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

class AccountAPI(viewsets.ModelViewSet):
	serializer_class=AccountSerializer
	queryset = Accounts.objects.all()

@csrf_exempt
def check_credentials(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        
        email = data.get('account_email')
        password = data.get('account_password')

        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM fwm_account a JOIN fwm_customer b ON a.account_id = b.cus_account JOIN fwm_address c ON b.cus_address = c.address_id WHERE account_email = %s AND account_password = %s",
            [email, password]
        )
        user = cursor.fetchall()

        cursor.execute(
            "SELECT * FROM fwm_account a JOIN fwm_organization b ON a.account_id = b.org_account JOIN fwm_address c ON b.org_address = c.address_id WHERE account_email = %s AND account_password = %s",
            [email, password]
        )
        userOrg = cursor.fetchall()

        cursor.execute(
            "SELECT * FROM fwm_account a JOIN fwm_vendor b ON a.account_id = b.vendor_account JOIN fwm_address c ON b.vendor_address = c.address_id WHERE account_email = %s AND account_password = %s",
            [email, password]
        )
        userVen = cursor.fetchall()

        user_type = data.get("user_type")
        if user:
            full_name = user[0][2] 
            coords = user[0][-1]
            accType = user[0][6]
            cursor.execute(
                "SELECT LatiLong FROM fwm_address a JOIN fwm_vendor b ON a.address_id = b.vendor_address"
            )
            vendor_addresses = cursor.fetchall()
            return JsonResponse({'valid': True, 'full_name': full_name, 'coords': coords, 'type': accType, 'addresses': vendor_addresses})
        elif userOrg:
            full_name = userOrg[0][2] 
            coords = userOrg[0][-1]
            accType = userOrg[0][6]
            cursor.execute(
                "SELECT LatiLong FROM fwm_address a JOIN fwm_vendor b ON a.address_id = b.vendor_address"
            )
            vendor_addresses_1 = cursor.fetchall()
            return JsonResponse({'valid': True, 'full_name': full_name, 'coords': coords, 'type': accType, 'addresses': vendor_addresses_1})
        elif userVen:
            full_name = userVen[0][2] 
            coords = userVen[0][-1]
            accType = userVen[0][6]
            cursor.execute(
                "SELECT LatiLong FROM fwm_address a JOIN fwm_organization b ON a.address_id = b.org_address"
            )
            org_addresses = cursor.fetchall()
            return JsonResponse({'valid': True, 'full_name': full_name, 'coords': coords, 'type': accType, 'addresses': org_addresses})
        else:
            return JsonResponse({'valid': False})
    else:
        return JsonResponse({}, status=405)

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        
        # Extracting data from the request
        fullname = data.get('account_name')
        #username = data.get('username')
        email = data.get('account_email')
        password = data.get('account_password')
        contactNum = data.get('account_contact')
        userType = data.get('account_type')
        latLong = data.get('latitude_long')
       

        # Insert the user into the database
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO fwm_account (account_name, account_email, account_password, account_contact, account_type) VALUES (%s, %s, %s, %s, %s)",
            [fullname, email, password, contactNum, userType]
        )
        connection.commit()

        cursor.execute("SELECT LAST_INSERT_ID()")
        last_id = cursor.fetchone()

        cursor.execute("INSERT INTO fwm_address(LatiLong) VALUES (%s)", [latLong])
        connection.commit()

        cursor.execute("SELECT LAST_INSERT_ID()")
        last_address_id = cursor.fetchone()
        
        if userType.lower() == "customer":
            cursor.execute(
                "INSERT INTO fwm_customer (cus_name, cus_address, cus_account) VALUES (%s, %s, %s)",
                [fullname, last_address_id, last_id]
            )
        elif userType.lower() == "organization":
            cursor.execute(
                "INSERT INTO fwm_organization (org_name, org_address, org_account) VALUES (%s, %s, %s)",
                [fullname, last_address_id, last_id]
            )
        elif userType.lower() == "vendor":
            cursor.execute(
                "INSERT INTO fwm_vendor (vendor_name, vendor_address, vendor_account) VALUES (%s, %s, %s)",
                [fullname, last_address_id, last_id]
            )
        
        connection.commit()

        return JsonResponse({'valid': True, 'message': 'User created successfully'})
    else:
        return JsonResponse({}, status=405)

@csrf_exempt
def placeOrder(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        # Extracting data from the request
        productName = data.get('product_name')
        productPrice = data.get('product_price')
        productQuantity = data.get('product_quantity')
        productImage = data.get('product_image')
       
        # Insert the user into the database
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO fwm_products (prod_name, prod_price, prod_quantity, product_image) VALUES (%s, %s, %s, %s)",
            [productName, productPrice, productQuantity, productImage]
        )
        connection.commit()
        return JsonResponse({'valid':True, 'message': 'Product uploaded successfully'})
    else:
        return JsonResponse({}, status=405)





