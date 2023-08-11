from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from .models import MenuItem,Order
from .forms import MenuItemForm , OrderForm

def menu_list(request):
    menu_items = MenuItem.objects.all()
    print(menu_items)
    return render(request, 'menu_list.html', {'menu_items': menu_items})


def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_list')
    else:
        form = MenuItemForm()
    return render(request, 'add_menu_item.html', {'form': form})

def update_menu_item(request, pk):
    item = get_object_or_404(MenuItem, id=pk)
    item.availability = not item.availability  # Toggle the availability status
    item.save()
    return redirect('menu_list')

def delete_menu_item(request, pk):
    menu_item = MenuItem.objects.get(id=pk)
    try:
        menu_item.delete()
        return redirect('menu_list')
    except:
        return redirect('menu_list')
    # return render(request, 'delete_menu_item.html', {'menu_item': menu_item})

def take_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            customer_name = form.cleaned_data['customer_name']
            selected_items = form.cleaned_data['selected_items']
            total_price = sum(item.price for item in selected_items)

            # Create an order record in the database
            order = Order.objects.create(
                cust_name=customer_name,
                price=total_price,
                order_status='recieved'
            )
            order.menu_items.set(selected_items)  # Set the selected menu items for the order

            # Process the order and update order status as needed
            # ...

            return redirect('menu_list')  # Redirect to the menu list after processing
    else:
        form = OrderForm()

    return render(request, 'take_order.html', {'form': form})