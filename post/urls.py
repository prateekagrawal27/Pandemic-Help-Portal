from django.contrib import admin
from django.urls import path

from . import views
from django.urls import include


app_name = 'post'
urlpatterns= [
    path('createpost', views.Createpost.as_view(), name="createpost"),
    path('mypost', views.MyPosts.as_view(), name="mypost"),
    path('', views.postList.as_view(), name="postlist"),
    path('<pk>:\editpost', views.UpdatePost.as_view(), name="editpost"),
    path('<pk>:\delete', views.DeletePost.as_view(), name="deletepost"),
    path('mypost', views.MyPosts.as_view(), name="mypost"),
    path('VC',views.VC,name='vaccination_centre'),
    path('showresult',views.showresult,name='showresult')
] 
