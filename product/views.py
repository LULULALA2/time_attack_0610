from django.shortcuts import render
from .models import Category, Product, ProductOrder, OrderStatus, UserOrder

# Create your views here.
def category_view(request):
    categories = Category.objects.all()
    infos = {}
    for category in categories:
        infos[category.name] = Product.objects.filter(category=category).count()
    return render(request, 'category.html', {'infos': infos})


def product_view(request, category_id):
    products = Category.POST.filter(id=category_id)
    return render(request, 'list.html', {'products': products})