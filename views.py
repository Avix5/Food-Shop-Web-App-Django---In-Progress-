from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

# @login_required
# function based view

# def index(request):
#     # getting data from database
#     item_list=item.objects.all()
#     # return HttpResponse(item_list)
#     # creating context
#     context={
#         'item_list':item_list
#     }
#     # passing context to html
#     return render(request,"myapp/index.html",context)


# class based view
class IndexClassView(ListView):
    model=item
    template_name="myapp/index.html"
    context_object_name='item_list'

# getting data on the basis of id
# def detail(request,id):
#     Item=item.objects.get(id=id)
#     # return HttpResponse(f"this is detail view of id {Item}")
#     context={
#         'item':Item
#     }
#     return render(request,"myapp/details.html",context)

# class based vieew
class FoodDetail(DetailView):
    model=item
    template_name="myapp/details.html"
    context_object_name='item'



def item_view(request):
    return HttpResponse("this is an item")

def create_item(request):
    if request.method=="POST":
        form=ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        # print("post is trigerred")
        # print(request.POST)
    form =ItemForm()
    context={
        "form":form
    }
    return render(request,"myapp/item-form.html",context)

def update_item(request,id):    
    # print("you can edit product of id",id)
    Item=item.objects.get(id=id)
    form=ItemForm(request.POST or None,instance=Item)
    if form.is_valid():
        form.save()
        return redirect('index')
    context={
        "form":form
    }
    return render(request,'myapp/item-form.html',context)

def delete_item(request,id):
    Item=item.objects.get(id=id)
    if request.method=="POST":
        Item.delete()
        return redirect("index")
    
    return render(request,'myapp/delete.html')
