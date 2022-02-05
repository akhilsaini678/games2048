from ast import operator
from django_unicorn.components import UnicornView
import random
import copy


# Function to select a random index which is empty and put either 2 or 4 randomly.
def random_box_slection(arr):
    ls=[]
    rand_num = [2,4]
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            if arr[i][j]==0:
                ls.append((i,j))
    if len(ls)!=0:
        index = random.choice(ls)
        arr[index[0]][index[1]]=random.choice(rand_num)
        




# Function to copy element from temporary array to main array
def fun_copy(arr,tmp,operation,i):
    if operation=="Up" or operation=="Down":
        for j in range(0,len(tmp)):
            arr[j][i]=tmp[j]
    else:
        arr[i]=tmp


# Function if left arrow is pressed.
def shift(arr,score,operation):
    start,end,direction=0,0,0
    Num=len(arr[0])

    if operation=="Left" or operation=="Up":
        start,end,direction = 0,Num,1
    elif operation=="Right" or operation=="Down":
        start,end,direction = Num-1,-1,-1
    

    for i in range(0,len(arr)):
        tmp = [0]*Num
        index=start
        for j in range(start,end,direction):
            i1=copy.copy(i)
            j1=copy.copy(j)
            if operation=="Up" or operation=="Down":
                i1,j1 = j1,i1

            if arr[i1][j1]!=0:
                tmp[index]=arr[i1][j1]
                index+=direction
        
        fun_copy(arr,tmp,operation,i)

    

    for i in range(0,len(arr)):
        tmp = [0 for i in range(Num)]
        index = start
        j=start
        while j != end:
            i1=copy.copy(i)
            j1=copy.copy(j+direction)
            i2=copy.copy(i)
            j2=copy.copy(j)
            if operation=="Up" or operation=="Down":
                i1,j1 = j1,i1
                i2,j2 = j2,i2

            if j!=(end-direction) and arr[i1][j1]==arr[i2][j2]:
                tmp[index]=arr[i2][j2]*2
                score[0]+=int(tmp[index])
                j+=direction
            else :
                tmp[index]=arr[i2][j2]

            j+=direction
            index+=direction
        
        fun_copy(arr,tmp,operation,i)



def reset_all(arr,score):
    score[0]=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j]=0
    random_box_slection(arr)
    random_box_slection(arr)



class Component1View(UnicornView):
    num = 0
    arr = [[]]
    score=0

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  # calling super is required
        self.num = kwargs.get("number")
        self.arr= kwargs.get("array")
        self.score= [kwargs.get("scores")]
        random_box_slection(self.arr)
        random_box_slection(self.arr)

    
    def shifting(self,operation):
        shift(self.arr,self.score,operation)
        random_box_slection(self.arr)


    def reset(self):
        reset_all(self.arr,self.score)
        











# # def right_shift(arr):
# def right_shift(arr,score):
#     for i in range(0,len(arr)):
#         tmp = [0 for i in range(len(arr[i]))]
#         index = len(arr[i])-1 
#         for j in range(len(arr[i])-1,-1,-1):
#             if arr[i][j]!=0:
#                 tmp[index]=arr[i][j]
#                 index-=1
#         arr[i]=tmp

    

#     for i in range(0,len(arr)):
#         tmp = [0 for i in range(len(arr[i]))]
#         index = len(arr[i])-1
#         j = len(arr[i])-1
#         while j>0:
#             if j!=0 and arr[i][j-1]==arr[i][j]:
#                 tmp[index]=arr[i][j]*2
#                 score[0]+=int(tmp[index])
#                 index-=1
#                 j-=1
#             else :
#                 tmp[index]=arr[i][j]
#                 index-=1
#             j-=1
#         arr[i]=tmp


# def up_shift(arr):
# Function if up arrow is pressed.
# def up_shift(arr,score):
#     for i in range(0,len(arr)):
#         tmp = [0 for i in range(len(arr[i]))]
#         index = 0 
#         for j in range(0,len(arr[i])):
#             if arr[j][i]!=0:
#                 tmp[index]=arr[j][i]
#                 index+=1
        
#         for j in range(0,len(tmp)):
#             arr[j][i]=tmp[j]

    

#     for i in range(0,len(arr)):
#         tmp = [0 for i in range(len(arr[i]))]
#         index = 0 
#         j=0
#         while j<len(arr[i]):
#             if j!=(len(arr[i])-1) and arr[j+1][i]==arr[j][i]:
#                 tmp[index]=arr[j][i]*2
#                 score[0]+=int(tmp[index])
#                 index+=1
#                 j+=1
#             else :
#                 tmp[index]=arr[j][i]
#                 index+=1
#             j+=1
#         for j in range(0,len(tmp)):
#             arr[j][i]=tmp[j]

# # def down_shift(arr):
# def down_shift(arr,score):
#     for i in range(0,len(arr)):
#         tmp = [0 for i in range(len(arr[i]))]
#         index = len(arr[i])-1 
#         for j in range(len(arr[i])-1,-1,-1):
#             if arr[j][i]!=0:
#                 tmp[index]=arr[j][i]
#                 index-=1
        
#         for j in range(len(tmp)-1,-1,-1):
#             arr[j][i]=tmp[j]

    

#     for i in range(0,len(arr)):
#         tmp = [0 for i in range(len(arr[i]))]
#         index = len(arr[i])-1
#         j= len(arr[i])-1
#         while j>0:
#             if j!=0 and arr[j-1][i]==arr[j][i]:
#                 tmp[index]=arr[j][i]*2
#                 score[0]+=int(tmp[index])
#                 index-=1
#                 j-=1
#             else :
#                 tmp[index]=arr[j][i]
#                 index-=1
#             j-=1
#         for j in range(len(tmp)-1,-1,-1):
#             arr[j][i]=tmp[j]

# # def down_shift(arr):