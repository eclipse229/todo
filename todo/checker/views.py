from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .models import Checker


# Create your views here.
class ListViews(ListView):
    queryset = Checker.objects.all()
    context_object_name = 'checker'
    paginate_by = 2
    template_name ='checker/list.html'

def details(request,id,title):
    checker =get_object_or_404(status='uncompleted',
                               date__id =id,
                               date__title = title,
                                                     )
    return render(request, 'checker/details.html',{'checker':checker})
