from . import views

from django.urls import path



urlpatterns = [
    path('', views.allproducts, name='allproducts'),
    path('<slug:slug_c>/', views.allproducts, name='product_by_category'),
    path('<slug:slug_c>/<slug_p>/', views.prod_det, name='product_catdetail'),

    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
    path('payments/', views.payments, name='payments'),
    path('base/', views.base, name='base'),
]
