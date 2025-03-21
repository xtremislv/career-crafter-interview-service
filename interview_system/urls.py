from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='carteer_home'),
    path('submit',views.submit,name='submit'),
    path('carteer_login.html',views.login,name='carteer_login'),
    path('carteer_register.html',views.register,name='carteer_register'),
    path('logout.html',views.logout,name='logout'),
    path('carteer_contactus.html',views.contact,name='carteer_contactus'),
    path('account.html',views.account,name='account'),
    path('interview.html',views.interview,name='interview')
    ]