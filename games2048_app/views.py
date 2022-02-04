from django.shortcuts import render
import math
import random


rand_num = [2,4]

# Function to select a random index which is empty and put either 2 or 4 randomly.
def random_box_slection(arr):
    ls=[]
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            if arr[i][j]==0:
                tmp=[]
                tmp.append(i)
                tmp.append(j)
                ls.append(tmp)
    if len(ls)!=0:
        index = random.choice(ls)
        arr[index[0]][index[1]]=random.choice(rand_num)






# Create your views here.
def index(request):
    N=4
    rows, cols = (N, N)
    arr = [[0 for i in range(cols)] for j in range(rows)]
    random_box_slection(arr)
    return render(request,'index.html',{'arr':arr})