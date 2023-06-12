from django.urls import path     
from . import views

urlpatterns = [ 
    path('', views.index)  ,
    path('Reg', views.Registration) , 
    path('All', views.get_all_users) ,
    path('deleteuser/<int:id>', views.delete_user) ,
    path('edituser/<int:id>', views.edituser) ,
    path('edituserpost', views.editpost) 
]
