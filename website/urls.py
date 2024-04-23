from django.urls import path
from .import views 


urlpatterns= [
    path('', views.home, name='home'),
   
   # path('login', views.login_user,name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>', views.customer_record, name='customer_record'),
    path('delete/<int:pk>', views.delete_customer, name='delete_record'),
    path('update/customer/<int:pk>', views.update_record, name='update_record'),
    path('add/customer/', views.add_customer, name='add_customer'),
    path('add/member/', views.creaMember, name='add_member'),
    path('view/member/<int:pk>', views.member_record, name='view_member'),
 
]
handler404 = 'views.custom_404'