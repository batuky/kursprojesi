from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    # path('<int:blog id>',views.blogdetail, name='detail'),
]
