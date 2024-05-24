# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Accounts(models.Model):
	account_id = models.IntegerField(primary_key=True)
	account_email = models.CharField(max_length=255)
	account_password = models.CharField(max_length=255)
	account_username = models.CharField(max_length=255)
	account_contact = models.CharField(max_length=255)

	class Meta:
		managed=False
		db_table='fwm_account'

class Address(models.Model):
	address_id = models.IntegerField(primary_key=True, max_length=11)
	street = models.CharField(max_length=255)
	barangay = models.CharField(max_length=255)
	municipality = models.CharField(max_length=255)
	province = models.CharField(max_length=255)
	zip_code = models.CharField(max_length=255)

	class Meta:
		managed=False
		db_table = 'fwm_address'
	
class Vendor(models.Model):
	vendor_id = models.IntegerField(primary_key=True, max_length=11)
	vendor_name = models.CharField(max_length=40)
	vendor_address = models.ForeignKey('Address', models.DO_NOTHING, db_column='vendor_address')
	vendor_account = models.CharField(unique=True, max_length = 13)
	
	class Meta:
		managed = False
		db_table = 'fwm_vendor'

class Customer(models.Model):
	cus_id = models.IntegerField(primary_key=True, max_length=11)
	cus_name = models.CharField(max_length=255)
	cus_contact = models.CharField(unique=True, max_length=13)
	cus_email = models.CharField(unique=True, max_length=255)
	cus_address = models.ForeignKey('Address', models.DO_NOTHING, db_column='cus_address')
	cus_uname = models.CharField(unique=True, max_length=20)

	class Meta:
		managed = False
		db_table = 'fwm_customer'

class Organization(models.Model):
	org_id = models.IntegerField(primary_key=True, max_length=11)
	org_name = models.CharField(max_length=255)
	org_contact = models.CharField(unique=True, max_length=13)
	org_email = models.CharField(unique=True, max_length=255)
	org_address = models.ForeignKey('Address', models.DO_NOTHING, db_column='org_address')
	org_uname = models.CharField(unique=True, max_length=20)

	class Meta:
		managed = False
		db_table='fwm_organization'

class Products(models.Model):
	prod_id = models.IntegerField(primary_key=True, max_length=11)
	prod_name = models.CharField(max_length=255)
	vendor_id = models.ForeignKey('Vendor', models.DO_NOTHING, db_column='vendor_id')
	prod_price = models.FloatField()
	prod_quantity = models.IntegerField(max_length=11)
	product_image = models.CharField(max_length=255)

	class Meta:
		managed=False
		db_table="fwm_products"
	
class Orders(models.Model):
	order_id = models.IntegerField(primary_key=True, max_length=11)
	order_refNum = models.CharField(max_length=255)
	setter_id = models.ForeignKey('Customer', models.DO_NOTHING, db_column = 'setter_id')
	#setter_id = models.ForeignKey('Organization', models.DO_NOTHING, db_column='org_setter_id')
	product_id = models.ForeignKey('Products', models.DO_NOTHING, db_column = 'product_id')
	vendor_id = models.ForeignKey('Vendor',models.DO_NOTHING,related_name='+', db_column="vendor_id")
	order_date = models.DateField()

	class Meta:
		managed=False
		db_table='fwm_orders'


