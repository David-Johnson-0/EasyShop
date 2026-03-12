from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('item/', views.item, name='item'),
    path('checkout/', views.checkout, name='checkout'),
    path('account/', views.account, name='account'),
    path('settings/', views.settings, name='settings'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
]
