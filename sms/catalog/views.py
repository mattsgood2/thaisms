from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Menu
from cart.forms import CartAddMenuForm
# Create your views here.

class MenuListView(ListView):
    model = Menu
    #context_object_name = 'menu_page'

class MenuDetailView(DetailView):
    model = Menu
    cart_menu_form = CartAddMenuForm()
    # menu = get_object_or_404(Menu, id=id, slug=slug)
# def product_list(request, category_slug=None):
#     category = None
#     menu = Menu.objects.all()
#     # products = Product.objects.filter(available=True)
#     if menu_slug:
#         menu = get_object_or_404(Menu, slug=menu_slug)
#         menu = Menu.objects.filter(menu=menu)
#
#     context = {
#         'menu': menu,
        # 'categories': categories,
        # 'products': products
    # }
    # return render(request, 'catalog/product/list.html', context)


####################################
#def index(request):
#    return HttpResponse("Hello, world. You're at the Menu index.")
################################################


#######################################
#testing only
