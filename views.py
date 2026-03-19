from django.shortcuts import render
from django.http import HttpResponse
from .models import item
# Create your views here.

def index(request):
    # getting data from database
    item_list=item.objects.all()
    # return HttpResponse(item_list)
    # creating context
    context={
        'item_list':item_list
    }
    # passing context to html
    return render(request,"myapp/index.html",context)

# getting data on the basis of id
def detail(request,id):
    Item=item.objects.get(id=id)
    # return HttpResponse(f"this is detail view of id {Item}")
    context={
        'item':Item
    }
    return render(request,"myapp/details.html",context)


def item_view(request):
    return HttpResponse("this is an item")