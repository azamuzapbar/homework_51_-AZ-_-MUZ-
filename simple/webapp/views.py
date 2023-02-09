from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'index.html')

def add_view(request:WSGIRequest):
    if request.method == 'GET':
        return render (request, 'index.html')
    print(request.POST)
    context = {
        'name': request.POST.get('name')
    }
    return render(request, 'indextwo.html', context=context)

