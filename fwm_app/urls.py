from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from employee_app import views

router = routers.DefaultRouter()

router.register('address', views.AddressAPI)
router.register('vendor', views.VendorAPI)
router.register('organizations', views.OrganizationAPI)
router.register('customer', views.CustomerAPI)
router.register('orders', views.OrdersAPI)
router.register('product', views.ProductAPI)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
