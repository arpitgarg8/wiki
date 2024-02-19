from django.urls import path

from . import views
app_name="encyclopedia"

urlpatterns =[
    path("", views.index, name="index"),
    path("search/",views.search,name="search"),
    path("new",views.newentry,name='newentry'),
    path("edit_true=<str:title>",views.editentry,name='editentry'),
    path("random",views.randompage,name="randompage"),
    path("<str:entryname>",views.viewentry,name="viewentry"),
    
     ]


