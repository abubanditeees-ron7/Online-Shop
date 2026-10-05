from django.shortcuts import render
from .models import Category, Product


def home(request):
    categories = Category.objects.all()

    featured_products = Product.objects.filter(
        is_available=True,
        is_featured=True
    )[:8]

    context = {
        'categories': categories,
        'featured_products': featured_products,
    }

    return render(
        request,
        'store/home.html',
        context
    )