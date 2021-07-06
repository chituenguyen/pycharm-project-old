from django.contrib import admin
from django.urls import path, include
from .views import HomeView, ProductDetailView, CheckoutView, add_to_cart, remove_from_cart, OrderSummaryView, \
    add_element_to_cart, remove_element_to_cart, trash, add_coupon, RefundView

app_name = 'core'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('product/<slug>/', ProductDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('add-element-to-cart/<slug>', add_element_to_cart, name='add-element'),
    path('remove-element-to-cart/<slug>', remove_element_to_cart, name='remove-element'),
    path('trash/<slug>', trash, name='trash'),
    path('add-coupon/', add_coupon, name='add-coupon'),
    path('refund/', RefundView.as_view(), name='refund')
]
