from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm
from django.views.generic.list import ListView

# Create your views here.
class IndexView(ListView):
    queryset = User.objects.order_by("last_name")

def add(request):
    if request.method == "POST":
        userForm = UserForm(request.POST, request.FILES)
        if userForm.is_valid():
            new_user = userForm.save()
            return redirect("login:index")
    else:
        userForm = UserForm()
        return render(request, "login/add.html", 
            {"userForm": userForm})