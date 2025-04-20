from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.all_chai,name='all_chai'),
    path('',views.blog_list, name='blog_list'),
    path('<int:blog_id>/del/',views.blog_del, name='blog_del'),
    path('<int:blog_id>/edit/',views.blog_edit, name='blog_edit'),
    path('create/',views.blog_create, name='blog_create'),
    path('register/',views.register, name='register'),
]


