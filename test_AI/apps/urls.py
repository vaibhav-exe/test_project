from django.urls import path
from .views import *

urlpatterns = [
    #path("route_naming", function_name, name="any_prefered_name") 
    path("",index,name="index"),
    path("create/", to_do_create, name="to_do_create"),
    path("list/", to_do_list, name="to_do_list"),
    path("update/", to_do_update, name="to_do_update"),
    path("view/", to_do_view, name="to_do_view"),
    
]
