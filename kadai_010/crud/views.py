from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class Topview(TemplateView):
    template_name = "top.html" #返したいhtmlを変数に代入　template_nameは名前は固定 クラス変数だから。

class ABCview(TemplateView):
    template_name = "abc.html" #返したいhtmlを変数に代入　template_nameは名前は固定

class ProductListView(ListView):
    model = Product
    paginate_by = 3

class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"

class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    template_name_suffix = "_update_form"

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("list")

class ProductDetailView(DetailView):
    model = Product
    template_name = "crud/product_detail.html"
