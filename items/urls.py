from django.urls import path
from . import views   

urlpatterns = [
    path("lostitems/", views.lostItems.as_view(), name="lostItems"),
]

app_name = "items"