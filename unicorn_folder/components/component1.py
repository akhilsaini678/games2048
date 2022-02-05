from ast import operator
from django_unicorn.components import UnicornView
import random
import copy


# Condition for winning 
Win_Score = 2048



#                                Function 1 : Checking if game is over or not 

# Function to check if game is over or not.
# Checking all four surrounding of each cell,
# if any of the matching with surrounding then game is not over.
def check_gameover(matrix):

    for i in range(len(matrix)): 
        for j in range(len(matrix[i])):
            if i+1<len(matrix) and matrix[i][j] == matrix[i+1][j]:
                    return True
            if i-1>=0 and matrix[i][j] == matrix[i-1][j]:
                    return True
            if j+1<len(matrix) and matrix[i][j] == matrix[i][j+1]:
                    return True
            if j-1>=0 and matrix[i][j] == matrix[i][j-1]:
                    return True

    return False

















#                              Function 2 : Putting a random value in one of the empty cell randomly

# Function to select a random index which is empty and put either 2 or 4 randomly.
def random_box_slection(matrix,score,game_over):

    # Element to be put randomly.
    rand_choice = [2,4]

    # Temprorary list for storing empty index
    tmp_list = []

    # Checking if any cell is left empty or not
    empty_box = 0

    # Putting all empty cell into tmp_list  
    for i in range(len(matrix)): 
        for j in range(len(matrix[i])): 
            if matrix[i][j] == 0:
                tmp_list.append((i,j))
                empty_box+=1

            # If any cell become Equal to 2048 then game is over and player win
            if matrix[i][j] == Win_Score:
                game_over[0]=2
                return


    # If there is any empty position and game is not over yet then, 
    # put random value on any random index from the tmp_list
    if len(tmp_list)!=0 and game_over[0] == 0:
        random_index = random.choice(tmp_list)
        matrix[random_index[0]][random_index[1]]=random.choice(rand_choice)

    
    # If the game is over or not , idea behind this : If there was only 1 empty box then we would have
    # put something in it, so now we have fully filled matrix, so I am going to check for each index if 
    # any index can be shift or not
    # If there is more than 1 empty box then it doesn't require to check.
    if empty_box == 1 and check_gameover(matrix) == False:
        game_over[0]=1















#                  Function 3 : Copying temporary array to main matrix after shifting operation

# Function to copy element from temporary array to main matrix
def fun_copy(matrix,tmp_array,operation,index):

    # If operation is left or right, then simply copying the complete
    # row into main matrix will give us the required result
    # Else I am copying values of tmp_array column-wise into the main array

    if operation=="Left" or operation=="Right":
        matrix[index]=tmp_array
    else:
        for j in range(0,len(tmp_array)):
            matrix[j][index]=tmp_array[j]
















#                Function 4 : Doing shifting operation and merging consecutive same value.
#                             First loop do shift operation and second loop merge consecutive same element


# Function for shifting.
def shift(matrix,score,operation):
    startIndex,endIndex,direction=0,0,0
    Size=len(matrix[0])

    matrix_copy = copy.deepcopy(matrix)


    # Initializing , startIndex, endIndex, direction according to shift direction
    if operation=="Left" or operation=="Up" :
        startIndex, endIndex, direction = 0, Size, 1
    elif operation=="Right" or operation=="Down" :
        startIndex, endIndex, direction = Size-1, -1, -1



    # Shifting cell according to the operation
    for i in range(0,len(matrix)):

        tmp_array = [0]*Size          # A temporay list to store new values 
        index = startIndex            # Starting index for temporary list
        for j in range(startIndex, endIndex, direction):

            # Reason behind taking copies of i and j, is because in case of
            # of up and down, we need to work with column, so instead of having 
            # matrix[i][j] we need matrix[j][i], so I make a copy of i and j and 
            # swap them only when operation is up or down
            i1 = copy.copy(i)
            j1 = copy.copy(j)
            if operation == "Up" or operation == "Down":
                i1,j1 = j1,i1

            if matrix[i1][j1] != 0:
                tmp_array[index] = matrix[i1][j1]
                index+= direction
        

        # Function to copy all values into main matrix after shifting operation
        fun_copy(matrix, tmp_array, operation, i)

    


    # Checking if consecutive values after shifting are same and if it is same then merging them into one cell
    for i in range(0, len(matrix)):

        tmp_array = [0]*Size          # A temporay list to store new values 
        index = startIndex            # Starting index for temporary list

        j=startIndex

        while j != endIndex:
            # Reason behind taking copies of i and j, is because in case of
            # of up and down, we need to work with column, so instead of having 
            # matrix[i][j] we need matrix[j][i], so I make a copy of i and j and 
            # swap them only when operation is up or down  
            i1 = copy.copy(i)
            j1 = copy.copy(j)
            i2 = copy.copy(i)
            j2 = copy.copy(j+direction)
            if operation == "Up" or operation == "Down":
                i1,j1 = j1,i1
                i2,j2 = j2,i2


            # If consecutive value is same then we add it to the tmp_array and increase 
            # index by 1 and j by 2 otherwise put value into tmp_array as it is
            if j != (endIndex-direction) and matrix[i1][j1] == matrix[i2][j2]:
                tmp_array[index] = matrix[i1][j1]*2
                score[0]+= int(tmp_array[index])
                j+= direction
            else :
                tmp_array[index] = matrix[i1][j1]

            j+= direction
            index+= direction
        
        # Function to copy values into matrix after checking all consecutive similar values
        fun_copy(matrix, tmp_array, operation, i)
    


    # If matrix is still same as the matrix before shifting,
    # then it doesn't require to put a new random value so false is returned
    # otherwise true is returned and we can continue to generate a new value.
    if matrix!=matrix_copy:
        return True
    else:
        return False















#                    Function 5 : For resetting score and matrix values


def reset_all(matrix, score,game_over):
    # Reseting all values, score to 0 and matrix's all values to 0 and game_over to false
    # And then calling random function 2 times

    score[0] = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = 0

    game_over[0] = 0
    random_box_slection(matrix,score,game_over)
    random_box_slection(matrix,score,game_over)










#                                     Main Class



class Component1View(UnicornView):
    num = 0
    matrix = [[]]
    score = 0
    game_over = 0

    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)  # calling super is required
        
        # Initialising value after taking it from views.py and then 
        # calling random function two times

        self.num = kwargs.get("number")
        self.matrix= kwargs.get("matrixs")
        self.score= [kwargs.get("scores")]
        self.game_over=[0]
        random_box_slection(self.matrix,self.score,self.game_over)
        random_box_slection(self.matrix,self.score,self.game_over)

    

    # Function for shifting according to the operation = [ Left, Right, Up, Down ]
    def shifting(self,operation):

        # If game is not over then shift , and if while shifting, 
        # matrix changed then generate a new random value

        if self.game_over[0] == 0:
            if(shift(self.matrix, self.score, operation)):
                random_box_slection(self.matrix,self.score,self.game_over)



    # Function to reset all values to 0 in matrix and intialize only 2 random value
    def reset(self):
        reset_all(self.matrix,self.score,self.game_over)
        



















































# Code which I wrote before optimisation , where I was using different function for left, right, up, down shift.
# I just keep it here , to see the logic , how I generalised from it.


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
