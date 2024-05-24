from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from employee_app import views
from django.http import JsonResponse
from django.contrib.auth import authenticate

router = routers.DefaultRouter()

router.register('address', views.AddressAPI)
router.register('vendor', views.VendorAPI)
router.register('organizations', views.OrganizationAPI)
router.register('customer', views.CustomerAPI)
router.register('orders', views.OrdersAPI)
router.register('product', views.ProductAPI)
router.register('accounts', views.AccountAPI)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/check_credentials/', views.check_credentials, name='check_credentials'),
    path('api/signup/', views.signup, name='signup'),
    path('api/placeOrder/', views.placeOrder, name='place_order')
]
