from django.http import HttpResponse
from django.template import loader
from .models import Members
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .astar import astar,printoutput

def index(request):
  template = loader.get_template('test.html')
  return HttpResponse(template.render())
def addition(request):

    print( request.POST)
    num1 = request.POST['dd']
    city1 = request.POST.getlist('city 1')#read benefit values
    
    city2 = request.POST.getlist('city 2')#read weight values
    dist = request.POST.getlist('dist ')#read weight values
    ss = request.POST.getlist('city ')#read weight values
    h = request.POST.getlist('heursxtic ')#read weight values
    start=request.POST.get('start')
    end=request.POST.get('end')
    print(h)
    dist1= [int(i) for i in dist]# convert to int
    h1= [int(i) for i in h]# convert to int
    
    path,dd,expandedList=astar(start,end,city1,city2,dist1,ss,h1)
    finalpath=printoutput(start,end, path, dd, expandedList)

    print(num1)
    #benefit = request.form.getlist('benefit ')
    print(request.POST)
    return render(request, "result.html", {"result":finalpath})
  
