from django_unicorn.components import UnicornView
import random


check=0
rand_num = [2,4]
# score=int(0)

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



# Function if left arrow is pressed.
def left_shift(arr,score):
    for i in range(0,len(arr)):
        tmp = [0 for i in range(len(arr[i]))]
        index = 0 
        for j in range(0,len(arr[i])):
            if arr[i][j]!=0:
                tmp[index]=arr[i][j]
                index+=1
        arr[i]=tmp

    

    for i in range(0,len(arr)):
        tmp = [0 for i in range(len(arr[i]))]
        index = 0
        j=0 
        while j < len(arr[i]):
            if j!=(len(arr[i])-1) and arr[i][j+1]==arr[i][j]:
                tmp[index]=arr[i][j]*2
                score[0]+=int(tmp[index])
                # print(score)
                index+=1
                j+=1
            else :
                tmp[index]=arr[i][j]
                index+=1
            j+=1
        arr[i]=tmp

# def right_shift(arr):
def right_shift(arr,score):
    for i in range(0,len(arr)):
        tmp = [0 for i in range(len(arr[i]))]
        index = len(arr[i])-1 
        for j in range(len(arr[i])-1,-1,-1):
            if arr[i][j]!=0:
                tmp[index]=arr[i][j]
                index-=1
        arr[i]=tmp

    

    for i in range(0,len(arr)):
        tmp = [0 for i in range(len(arr[i]))]
        index = len(arr[i])-1
        j = len(arr[i])-1
        while j>0:
            if j!=0 and arr[i][j-1]==arr[i][j]:
                tmp[index]=arr[i][j]*2
                score[0]+=int(tmp[index])
                index-=1
                j-=1
            else :
                tmp[index]=arr[i][j]
                index-=1
            j-=1
        arr[i]=tmp

# def up_shift(arr):
# Function if up arrow is pressed.
def up_shift(arr,score):
    for i in range(0,len(arr)):
        tmp = [0 for i in range(len(arr[i]))]
        index = 0 
        for j in range(0,len(arr[i])):
            if arr[j][i]!=0:
                tmp[index]=arr[j][i]
                index+=1
        
        for j in range(0,len(tmp)):
            arr[j][i]=tmp[j]

    

    for i in range(0,len(arr)):
        tmp = [0 for i in range(len(arr[i]))]
        index = 0 
        j=0
        while j<len(arr[i]):
            if j!=(len(arr[i])-1) and arr[j+1][i]==arr[j][i]:
                tmp[index]=arr[j][i]*2
                score[0]+=int(tmp[index])
                index+=1
                j+=1
            else :
                tmp[index]=arr[j][i]
                index+=1
            j+=1
        for j in range(0,len(tmp)):
            arr[j][i]=tmp[j]

# def down_shift(arr):
def down_shift(arr,score):
    for i in range(0,len(arr)):
        tmp = [0 for i in range(len(arr[i]))]
        index = len(arr[i])-1 
        for j in range(len(arr[i])-1,-1,-1):
            if arr[j][i]!=0:
                tmp[index]=arr[j][i]
                index-=1
        
        for j in range(len(tmp)-1,-1,-1):
            arr[j][i]=tmp[j]

    

    for i in range(0,len(arr)):
        tmp = [0 for i in range(len(arr[i]))]
        index = len(arr[i])-1
        j= len(arr[i])-1
        while j>0:
            if j!=0 and arr[j-1][i]==arr[j][i]:
                tmp[index]=arr[j][i]*2
                score[0]+=int(tmp[index])
                index-=1
                j-=1
            else :
                tmp[index]=arr[j][i]
                index-=1
            j-=1
        for j in range(len(tmp)-1,-1,-1):
            arr[j][i]=tmp[j]

# def down_shift(arr):


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

    
    def left(self):
        left_shift(self.arr,self.score)
        random_box_slection(self.arr)

    def right(self):
        right_shift(self.arr,self.score)
        random_box_slection(self.arr)

    def up(self):
        up_shift(self.arr,self.score)
        random_box_slection(self.arr)

    def down(self):
        down_shift(self.arr,self.score)
        random_box_slection(self.arr)

    def reset(self):
        reset_all(self.arr,self.score)
        