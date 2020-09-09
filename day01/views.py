import datetime
import pprint

from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse,JsonResponse



def view_test_func():
    return "django20"

class Foo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

# Create your views here.
def view_func(request):
    # print(request.POST['username'])
    # print(request.POST['password'])
    url = reverse("v1")
    return redirect(url)

def view_func_v1(request,version):

    return HttpResponse(content="Hello World{}".format(version))

def view_re_func(request):
    return HttpResponse(content="re world")

def view_template(request):
    return render(request,'demo.html',context={
        "username":"test",
        "foo":[n for n in range(10)],
        "dict0":{"name":"james","age":18,"job":"basketball"},
        "func":view_test_func(),
        "class":Foo("kobe",24),
    })

def view_template_2(request):
    return render(request,'filter.html',context={
        "name":"",
        "test_a2A":"TEST",
        "num1":10,
        "num2":20,
        "lis":[n for n in range(10)],
        "now":datetime.datetime.now,
    })

def view_template_3(request):
    return render(request,'day01.html')

def view_template_4(request,username):
    name = request.GET['username']
    return render(request,'user.html',context={
        'username':name
    })

def view_template_5(request):
    pprint.pprint(request.META)
    print(request.user)
    print(request.method)
    return render(request,'images.html')

def view_json(request):
    data = {
        "name":"詹姆斯",
        "age":35,
    }

    return JsonResponse(data=data,json_dumps_params={
        'ensure_ascii':False
    })