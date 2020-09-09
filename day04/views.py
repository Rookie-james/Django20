from django.shortcuts import render

# Create your views here.

def if_view(request,name):
    return render(request,'if.html',context={
        'name':name
    })

def for_view(request):
    return render(request, 'for.html', context={
        'for_list':[n for n in range(10)].append(None)
    })

def url_view(request,version):
    return render(request, 'url.html', context={
        'version':version,
    })

def base_view(request):
    return render(request,'view.html')

def include_view(request):
    return render(request,'include.html')