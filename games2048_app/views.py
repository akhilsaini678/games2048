from django.shortcuts import render

def index(request):    
    N=4
    rows, cols = (N, N)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    score=int(0)
    return render(request,'index.html',{'arr':arr,'num':N,'score':score})