from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Product

# Create your views here.
class ProductDetailView(DetailView):
    model = Product

class ProductListView(ListView):
    model = Product
    paginate_by = 3