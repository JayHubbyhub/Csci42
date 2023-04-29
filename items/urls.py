from django.urls import path
from django.conf.urls.static import static
from . import views   

urlpatterns = [
    path("lostitems/", views.lostItems.as_view(), name="lostItems"),
    path("founditems/", views.foundItems.as_view(), name="foundItems"),
    path("newLostItem/", views.newLostItem, name="newLostItem")
]

app_name = "items"