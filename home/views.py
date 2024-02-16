from django.shortcuts import render
from django.views.generic import TemplateView

from .models import DishCategory, Chef, Events, Gallery
from .forms import ReservationForm

class MainPageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reservation_form = ReservationForm()

        context['categories'] = DishCategory.objects.filter(is_visible=True)
        context['chefs'] = Chef.objects.filter(is_visible=True)
        context['events'] = Events.objects.filter(is_visible=True)
        context['gallery'] = Gallery.objects.filter(is_visible=True)
        context['reservation_form'] = reservation_form

        return context

    def post(self, request, *args, **kwargs):
        reservation_form = ReservationForm(request.POST)
        print('Test')
        if reservation_form.is_valid():
            print('Good')
            reservation_form.save()
            return render(request, 'index.html', {'reservation_form': reservation_form})
        else:
            print('Bad')
            return render(request, 'index.html', {'reservation_form': reservation_form})


# def main_page(request):
#     categories = DishCategory.objects.filter(is_visible=True)
#     chefs = Chef.objects.filter(is_visible=True)
#     events = Events.objects.filter(is_visible=True)
#     gallery = Gallery.objects.filter(is_visible=True)
#     context = {
#         'categories': categories,
#         'chefs': chefs,
#         'events': events,
#         'gallery': gallery,
#     }
#     return render(request, 'index.html', context=context)
