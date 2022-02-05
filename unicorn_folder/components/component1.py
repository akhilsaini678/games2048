from ast import operator
from django_unicorn.components import UnicornView
import random
import copy

Win_Score = 2048

def check_gameover(matrix):

    for i in range(len(matrix)): 
        for j in range(len(matrix[i])):
            if i+1<len(matrix) and matrix[i][j]==matrix[i+1][j]:
                    return True
            if i-1>=0 and matrix[i][j]==matrix[i-1][j]:
                    return True
            if j+1<len(matrix) and matrix[i][j]==matrix[i][j+1]:
                    return True
            if j-1>=0 and matrix[i][j]==matrix[i][j-1]:
                    return True

    return False


# Function to select a random index which is empty and put either 2 or 4 randomly.
def random_box_slection(matrix,score,game_over):

    rand_choice = [2,4]
    tmp_list = []
    empty_box = 0

    # Selecting a random position 
    for i in range(len(matrix)): 
        for j in range(len(matrix[i])): 
            if matrix[i][j] == 0:
                tmp_list.append((i,j))
                empty_box+=1
            if matrix[i][j] == Win_Score:
                game_over[0]=2
                return


    # If there is any empty position then put random value
    if len(tmp_list)!=0 and game_over[0] == 0:
        random_index = random.choice(tmp_list)
        matrix[random_index[0]][random_index[1]]=random.choice(rand_choice)
    
    # If the game is over or not , idea behind this if there was only 1 empty box then we would have
    # something in it, so now we have fully filled matrix, so I am going to check for each index if 
    # any index can be shift or not

    if empty_box==1 and check_gameover(matrix) == False:
        game_over[0]=1





# Function to copy element from temporary matrix to main matrix
def fun_copy(matrix,tmp_array,operation,index):

    if operation=="Left" or operation=="Right":
        matrix[index]=tmp_array
    else:
        for j in range(0,len(tmp_array)):
            matrix[j][index]=tmp_array[j]



# Function for shifting.
def shift(matrix,score,operation):
    startIndex,endIndex,direction=0,0,0
    Size=len(matrix[0])

    # Initializing , startIndex, endIndex, direction according to shift direction
    if operation=="Left" or operation=="Up" :
        startIndex, endIndex, direction = 0, Size, 1
    elif operation=="Right" or operation=="Down" :
        startIndex, endIndex, direction = Size-1, -1, -1
    

    for i in range(0,len(matrix)):
        tmp_array = [0]*Size
        index = startIndex
        for j in range(startIndex, endIndex, direction):
            i1 = copy.copy(i)
            j1 = copy.copy(j)
            if operation == "Up" or operation == "Down":
                i1,j1 = j1,i1

            if matrix[i1][j1] != 0:
                tmp_array[index] = matrix[i1][j1]
                index+= direction
        
        fun_copy(matrix, tmp_array, operation, i)

    

    for i in range(0, len(matrix)):
        tmp_array = [0 for i in range(Size)]
        index = startIndex
        j=startIndex
        while j != endIndex:
            i1 = copy.copy(i)
            j1 = copy.copy(j)
            i2 = copy.copy(i)
            j2 = copy.copy(j+direction)
            if operation == "Up" or operation == "Down":
                i1,j1 = j1,i1
                i2,j2 = j2,i2

            if j != (endIndex-direction) and matrix[i1][j1] == matrix[i2][j2]:
                tmp_array[index] = matrix[i1][j1]*2
                score[0]+= int(tmp_array[index])
                j+= direction
            else :
                tmp_array[index] = matrix[i1][j1]

            j+= direction
            index+= direction
        
        fun_copy(matrix, tmp_array, operation, i)



def reset_all(matrix, score,game_over):
    score[0] = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = 0
    game_over[0] = 0
    random_box_slection(matrix,score,game_over)
    random_box_slection(matrix,score,game_over)



class Component1View(UnicornView):
    num = 0
    matrix = [[]]
    score = 0
    game_over = 0

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  # calling super is required
        self.num = kwargs.get("number")
        self.matrix= kwargs.get("matrixs")
        self.score= [kwargs.get("scores")]
        self.game_over=[0]
        random_box_slection(self.matrix,self.score,self.game_over)
        random_box_slection(self.matrix,self.score,self.game_over)

    
    def shifting(self,operation):
        if self.game_over[0] == 0:
            shift(self.matrix, self.score, operation)
            random_box_slection(self.matrix,self.score,self.game_over)


    def reset(self):
        reset_all(self.matrix,self.score,self.game_over)
        






# def left_shift(arr,score):
#     for i in range(0,len(arr)):
#         tmp = [0 for i in range(len(arr[i]))]
#         index = 0 
#         for j in range(0,len(arr[i])):
#             if arr[i][j]!=0:
#                 tmp[index]=arr[i][j]
#                 index+=1
#         arr[i]=tmp

    

#     for i in range(0,len(arr)):
#         tmp = [0 for i in range(len(arr[i]))]
#         index = 0
#         j = 0
#         while j>0:
#             if j<len(arr[i])-1 and arr[i][j-1]==arr[i][j]:
#                 tmp[index]=arr[i][j]*2
#                 score[0]+=int(tmp[index])
#                 index+=1
#                 j+=1
#             else :
#                 tmp[index]=arr[i][j]
#                 index+=1
#             j+=1
#         arr[i]=tmp




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
