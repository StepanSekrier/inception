from django.shortcuts import render
from myapp.models import list, table

from django.http import HttpResponse



def index(request):
    #test = list.objects.filter(id = '2')
    return render(request, "webdesign.html", {"set":[1,2,3,4,5]})

def auth(request):
    if request.method == "POST":
        data = request.POST
        print(data["login"])
        print(data["pass"])
        new_user = User.objects.create_user()

def webdesign(request):
    data = list.objects.all()
    return render(request, 'webdesign.html', {"data": data})

def card (request,myid):
    data = id.objects.filter(id = myid)
    data = table.object.filter()
    print (len(data))
    if len(data) != 0:

        return render (request, id.html, {"id": data})
    else:
        return HttpResponse("пользователь не найден")  


# Create your views here.

