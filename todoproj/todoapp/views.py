from django.shortcuts import render, redirect
from .models import TodoModel

# Create your views here.


def index(request):
    if request.method == 'POST':
        post = TodoModel()
        post.first_name = request.POST.get('fname')
        post.last_name = request.POST.get('lname')
        post.phone = request.POST.get('phone')
        post.address = request.POST.get('address')
        post.save()

        return redirect('home')

    else:
        all_list = TodoModel.objects.all()
        return render(request, 'todoapp/index.html', {"alllist": all_list})


def delete_item(request, id):
    if request.method == 'POST':
        data = TodoModel.objects.get(pk=id)
        data.delete()
        return redirect('home')


def update_item(request, id):
    data = TodoModel.objects.get(id=id)
    did = data.id
    dfname = data.first_name
    dlname = data.last_name
    dphone = data.phone
    daddress = data.address

    return render(request, 'todoapp/update.html', {'fname': dfname, 'lname': dlname, 'phone': dphone, "address": daddress, 'did': did})


def update_item_second(request, id):
    if request.method == 'POST':
        data = TodoModel.objects.get(id=id)
        data.first_name = request.POST.get('fname')
        data.last_name = request.POST.get('lname')
        data.phone = request.POST.get('phone')
        data.address = request.POST.get('address')
        data.save()
        return redirect('/')
