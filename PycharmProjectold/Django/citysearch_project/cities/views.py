from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import City
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q


# Create your views here.
# def HomepageView(request):
#     return render(request,'home.html',)
class HomepageView(TemplateView):
    template_name = 'home.html'
# def SearchResultsView(request):
#     model=City
#     cities = City.objects.all()
#     return render(request, 'search.html',{'cities':cities})

class SearchResultsView(ListView):
    model = City
    template_name = 'search.html'
    def get_queryset(self):
        query=self.request.GET.get('q') #predicate, check null insensitive
        object_list=City.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list

# .exclude(
#     state__icontains='NY'
