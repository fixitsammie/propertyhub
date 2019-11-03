from django.shortcuts import render
from .models import Property
from django.core.paginator import Paginator
def homepage(request):
    latest=Property.objects.all().order_by("-id")[0:6]
    return render(request, 'home.html', {'latest': latest})


def search(request):
    query=request.GET.get('q','')
    results=[]
    if query:
        results=Property.objects.filter(name__icontains=query) 
    variables={'query':query,'results':results}    
    return render(request, 'search.html',variables)       

def single_property(request,pk):
    property_=Property.objects.get(id=pk)
    variables={'property':property_}    
    return render(request,'single_property.html',variables) 

def all_property(request):
    property_=Property.objects.all()
    paginator = Paginator(property_, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    assets = paginator.get_page(page)
    return render(request, 'all_property.html', {'property': assets})
 

