from django.shortcuts import redirect, render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


def home_page(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'mini/home.html', context)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'mini/add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'mini/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.doen = not item.doen
    item.save()
    return redirect('home')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('home')