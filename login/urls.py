from django.urls import path

from . import views   

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # login/users/add/
    path("users/add/", views.add, name="add"),
]

app_name = "login"