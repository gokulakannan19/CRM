from django.conf.urls import url
from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name="home"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('products/', views.products, name="products"),

    path('register/', views.register_page, name="register"),

    path('user/', views.user_page, name="user-page"),
    path('accounts/', views.account_settings, name="accounts"),

    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('create_order/<str:pk>/', views.create_order, name="create_order"),
    path('update_order/<str:pk>/', views.update_order, name="update_order"),
    path('delete_order/<str:pk>/', views.delete_order, name="delete_order"),
]
