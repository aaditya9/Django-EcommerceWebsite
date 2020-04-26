from django.shortcuts import render
from django.views.generic import ListView

from .models import Product
# Create your views here.

class productListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

def product_list_view(request):
	queryset = Product.objects.all()

	context = {
		'object_list' : queryset
	}
	print(context)
	return render(request,"products/list.html",context)


class productDetailView(ListView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

def product_detail_view(request, pk=None, *args, **kwargs):
	queryset = Product.objects.get(pk=pk)
	# instance = get_object_404(Product, pk=pk)
	context = {
		'object' : queryset
	}
	return render(request,"products/detail.html",context)