from django.shortcuts import render
from django.template import Template, Context
from .models import Item
from django.template.loader import get_template
from django.views import View

# Create your views here.
class lostItems(View):
    template = "lostitems.html"
    def get(self, request):
        all_lost_items = Item.objects.filter(isLost=True)
        context = {
            "all_lost_items": all_lost_items
        }
        
        return render(request, self.template, context)