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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_menu_form'] = CartAddMenuForm()
        return context



# def menu_detail(request, id, slug):
#     menu = get_object_or_404(Menu, id=id, slug=slug, available=True)
#     cart_menu_form = CartAddMenuForm()
#     context = {
#         'menu': menu,
#         'cart_product_form': cart_product_form
#     }
#     return render(request, 'catalog/menu_detail.html', context)

####################################
#def index(request):
#    return HttpResponse("Hello, world. You're at the Menu index.")
################################################


#######################################
#testing only
