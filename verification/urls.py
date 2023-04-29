from django.urls import path
from . import views   

urlpatterns = [
    path('', views.verification, name='verification'),
    path('display/', views.displayVerForms, name='displayverforms'),
    path('updateStatus/<int:pk>/<str:new_status>/', views.updateStatus, name='updateStatus'),
]

app_name = "verification"