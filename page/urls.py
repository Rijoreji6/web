from . import views
from django.urls import path


urlpatterns=[
    path('',views.home, name='home'),
    path('delete_num/<int:id>',views.delete_num,name='delete'),
    path('delete_str/<int:id>',views.delete_str, name='delstr'),
    path('delete_al/<int:id>',views.delete_al, name='delal'),

]