from django.urls import path
from . import views

# Create your url patterns here.

app_name = 'coupons'

urlpatterns = [
    path('apply/', views.coupon_apply, name='apply'),
]
