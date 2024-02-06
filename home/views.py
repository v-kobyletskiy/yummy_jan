from django.shortcuts import render
from .models import DishCategory


def main_page(request):
    categories = DishCategory.objects.filter(is_visible=True)
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)
