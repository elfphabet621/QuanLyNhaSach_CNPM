from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    # path('user/', views.userPage, name='user-page'),

    # path('account/', views.accountSetting, name='account'),

    # path('book/', views.products, name='products'),
    # path('customer/<str:pk_test>', views.customer, name='customer'),
    
    path('create_book/<str:pk>', views.createBook, name='create_Book'),
    path('update_book/<str:pk>', views.updateBook, name='update_Book'),
    path('delete_book/<str:pk>', views.deleteBook, name='delete_Book'),

]