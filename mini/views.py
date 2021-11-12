from django.shortcuts import redirect, render, redirect
from .models import Item

# Create your views here.


def home_page(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'mini/home.html', context)


def add_item(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, doen=done)

        return redirect('home')
    return render(request, 'mini/add_item.html')