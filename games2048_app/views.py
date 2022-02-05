from django.shortcuts import render
import math
import random
from django import forms



# Create your views here.
def index(request):
    
    N=4
    rows, cols = (N, N)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    score=int(0)
    return render(request,'index.html',{'arr':arr,'num':N,'score':score})