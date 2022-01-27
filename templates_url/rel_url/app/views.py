from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {'text':'hello world','number':100}
    return render(request,'app/index.html',my_dict)

def other(request):
    return render(request,'app/other.html')

def relative(request):
    return render(request,'app/rel_url_templates.html')

def test(request):
    return render(request,'app/test.html')
