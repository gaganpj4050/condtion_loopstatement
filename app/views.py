from django.shortcuts import render

# Create your views here.
def condtion(request):
    d={'a':190 ,'b':200 ,'c':300}
    return render(request,'condtion.html',d)

def loop(request):
    d={'name':'NAVEEN'}
    return render(request,'loop.html',d)