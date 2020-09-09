from django.shortcuts import render

# Create your views here.

def view_filter(request):
    return render(request, 'filters.html', context={
        "format_str":"%Y-%m-%d %H:%M:%S",
        "username":"james",
        "password":123456,
    })

def include_tag_view(request):
    return render(request, 'include_tag.html',context={
        'person':{
            'name':request.GET.get('name'),
            'age':request.GET.get('age'),
        },
        'person1': {
            'name': request.GET.get('name'),
            'age': request.GET.get('age'),
        },
    })

def include_tag_new(request):
    return render(request,'include_tag_new.html',context={
        'new':{
            'name':request.GET.get('new1'),
            'category':request.GET.get('new2'),
        }
    })