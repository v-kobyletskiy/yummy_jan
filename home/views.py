from django.shortcuts import render
from .models import DishCategory, Chef, Events, Gallery


def main_page(request):
    categories = DishCategory.objects.filter(is_visible=True)
    chefs = Chef.objects.filter(is_visible=True)
    events = Events.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    context = {
        'categories': categories,
        'chefs': chefs,
        'events': events,
        'gallery': gallery,
    }
    return render(request, 'index.html', context=context)
