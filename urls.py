from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('item',views.item),
    path('<int:id>/',views.detail,name='detail'),  
    # this is used to handel dynamic id 
]




# admin data
# name=abhishek
# pas=superuser
# mail=abhishek@gmail.com
# 