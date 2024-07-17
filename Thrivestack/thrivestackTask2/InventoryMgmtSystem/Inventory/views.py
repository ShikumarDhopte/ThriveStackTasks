from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from .forms import ItemForm


def item_list(request):
    items = Item.objects.all()
    return render(request, 'templates/item_list.html', {'items': items})


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = ItemForm()
    return render(request, 'templates/item_form.html', {'form': form})


def update_item(request, pk):
    post = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = ItemForm(instance=post)
    return render(request, 'templates/item_form.html', {'form': form})


def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('post_list')
    return render(request, 'templates/item_confirm_delete.html', {'item': item})
