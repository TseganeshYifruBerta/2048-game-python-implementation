import random
print("HEY Am Tseganesh Yifru from AAit do you want to play 2048 GAME")
''' this function controls the moving_positions of the tiles. It moves them up,down,left,right based on the choise'''
def moving_positions(gaming_box, choice):
   # *print("This is the first gaming_box ",gaming_box)
   if choice == "m":  # this if condition is used for the downward movement
       row = 0
       for column in range(0, 5):
           if gaming_box[row][column] != 0 or gaming_box[row + 1][column] != 0 or gaming_box[row + 2][column] != 0 or gaming_box[row + 3][column] != 0 or gaming_box[row + 4][column] != 0:  # This if statement basically checks if there is at least one number that is not zero in the column
               if gaming_box[row + 4][column] == 0:
                   while gaming_box[row + 4][column] == 0:# if the last number in the given column is zero
                       gaming_box[row + 4][column] = gaming_box[row +
                                                            3][column]
                       gaming_box[row + 3][column] = gaming_box[row2][column]# shift until the last number is not zero
                       gaming_box[row + 2][column] = gaming_box[row+1][column]
                       gaming_box[row + 1][column] = gaming_box[row][column]
                       gaming_box[row][column] = 0
               if gaming_box[row + 3][column] == 0 and (gaming_box[row+2][column] != 0  or gaming_box[row][column]!=0):
                   while gaming_box[row + 3][column] == 0:  # if the last number in the given column is zero
                       gaming_box[row + 3][column] = gaming_box[row + 2][
                           column]  # shift until the last number is not zero
                       gaming_box[row + 2][column] = gaming_box[row + 1][column]
                       gaming_box[row + 1][column] = gaming_box[row][column]
                       gaming_box[row][column] = 0
               if gaming_box[row + 2][column] == 0 and (gaming_box[row + 1][column] != 0 or gaming_box[row][
                   column] != 0):  # if the third number is zero and one of the numbers above it is a non-zero
                   while gaming_box[row + 2][column] == 0:
                       gaming_box[row + 2][column] = gaming_box[row + 1][column]
                       gaming_box[row + 1][column] = gaming_box[row][column]
                       gaming_box[row][column] = 0
                   # *print("THis is the second if statment",gaming_box)

               if gaming_box[row + 1][column] == 0 and gaming_box[row][
                   column] != 0:  # if the second number in a given column is zero while the number above is non-zero
                   while gaming_box[row + 1][column] == 0:
                       gaming_box[row + 1][column] = gaming_box[row][column]
                       gaming_box[row][column] = 0
               # * print("THis is the third if statment",gaming_box)
       row = 0
       for column in range(0, 5):
           if gaming_box[row + 4][column] == gaming_box[row + 3][column]:
               gaming_box[row + 4][column] = gaming_box[row + 4][column] + gaming_box[row + 3][column]
               gaming_box[row + 3][column] = gaming_box[row + 2][column]
               gaming_box[row + 2][column] = gaming_box[row + 1][column]
               gaming_box[row + 1][column] = gaming_box[row][column]
               gaming_box[row][column] = 0
           if gaming_box[row + 3][column] == gaming_box[row + 2][column]:
               gaming_box[row + 3][column] = gaming_box[row + 3][column] + gaming_box[row + 2][column]
               gaming_box[row + 2][column] = gaming_box[row + 1][column]
               gaming_box[row + 1][column] = gaming_box[row][column]
               gaming_box[row][column] = 0
           if gaming_box[row + 2][column] == gaming_box[row + 1][column]:
               gaming_box[row + 2][column] = gaming_box[row + 2][column] + gaming_box[row + 1][column]
               gaming_box[row + 1][column] = gaming_box[row][column]
               gaming_box[row][column] = 0
           if gaming_box[row + 1][column] == gaming_box[row][column]:
               gaming_box[row + 1][column] = gaming_box[row + 1][column] + gaming_box[row][column]
               gaming_box[row][column] = 0
   elif choice == "i":  # this code is for upward movement
       row = 0
       for column in range(0, 5):
           if gaming_box[row][column] != 0 or gaming_box[row + 1][column] != 0 or gaming_box[row + 2][column] != 0 or \
                   gaming_box[row + 3][
                       column] != 0 or gaming_box[row + 4][
               column] != 0:  # This if statement basically checks if there is at least one number that is not zero in the column
               if gaming_box[row][
                   column] == 0:  # this if statement is true only if the first number in a given column of column is zero
                   while gaming_box[row][column] == 0:
                       gaming_box[row][column] = gaming_box[row + 1][column]
                       gaming_box[row + 1][column] = gaming_box[row + 2][
                           column]  # the following statements basically shifts every number upward and inserts zero at the end
                       gaming_box[row + 2][column] = gaming_box[row + 3][column]
                       gaming_box[row + 3][column] = gaming_box[row + 4][column]
                       gaming_box[row + 4][column] = 0
                   # * print("THis is the first if",gaming_box)
               if gaming_box[row + 1][column] == 0 and (
                       gaming_box[row + 2][column] != 0 or gaming_box[row + 1][column] != 0 or gaming_box[row + 3][
                   column] != 0 or gaming_box[row + 4][
                           column] != 0):  # this if statement is true only if the second number in a given column column is zero and the other numbers under ihave aleast one non-zero value
                   while gaming_box[row + 1][column] == 0:
                       gaming_box[row + 1][column] = gaming_box[row + 2][column]
                       gaming_box[row + 2][column] = gaming_box[row + 3][column]
                       gaming_box[row + 3][column] = gaming_box[row + 4][column]
                       gaming_box[row + 4][column] = 0
                   # * delete to see print("This is the Second if",gaming_box)
               if gaming_box[row + 2][column] == 0 and (gaming_box[row + 3][column] != 0 or gaming_box[row + 4][
                   column] != 0):  # this if statement is true only if the third number in the column is zero and the number under it is not zero
                   while gaming_box[row + 2][column] == 0:
                       gaming_box[row + 2][column] = gaming_box[row + 3][column]
                       gaming_box[row + 3][column] = gaming_box[row + 4][column]
                       gaming_box[row + 4][column] = 0
               if gaming_box[row + 3][column] == 0 and gaming_box[row + 4][
                   column] != 0:  # this if statement is true only if the third number in the column is zero and the number under it is not zero
                   while gaming_box[row + 2][column] == 0:
                       gaming_box[row + 3][column] = gaming_box[row + 4][column]
                       gaming_box[row + 4][column] = 0
                   # * delete to see print("This is the third if",gaming_box)
       row = 0
       for column in range(0, 5):  # This part addes two numbers if they are identical
           if gaming_box[row][column] == gaming_box[row + 1][
               column]:  # if the first and second number in the colomn are identical
               gaming_box[row][column] = gaming_box[row][column] + gaming_box[row + 1][column]  # multiply it by 2
               gaming_box[row + 1][column] = gaming_box[row + 2][column]  # and shift upward
               gaming_box[row + 2][column] = gaming_box[row + 3][column]
               gaming_box[row + 3][column] = gaming_box[row + 4][column]
               gaming_box[row + 4][column] = 0
           if gaming_box[row + 1][column] == gaming_box[row + 2][
               column]:  # if the number second and third number in  the colomn column are identical
               gaming_box[row + 1][column] = gaming_box[row + 1][column] + gaming_box[row + 2][
                   column]  # multiply it by 2
               gaming_box[row + 2][column] = gaming_box[row + 3][column]
               gaming_box[row + 3][column] = gaming_box[row + 4][column]  # and shift upward
               gaming_box[row + 4][column] = 0
           if gaming_box[row + 2][column] == gaming_box[row + 3][column]:
               gaming_box[row + 2][column] = gaming_box[row + 2][column] + gaming_box[row + 3][column]
               gaming_box[row + 3][column] = gaming_box[row + 4][column]
               gaming_box[row + 4][column] = 0
           if gaming_box[row + 3][column] == gaming_box[row + 4][column]:
               gaming_box[row + 3][column] = gaming_box[row + 3][column] + gaming_box[row + 4][column]
               gaming_box[row + 4][column] = 0


   elif choice == "j":#this code is for left movement
       column = 0
       for row in range(0, 5):

           if gaming_box[row][column] != 0 or gaming_box[row][column + 1] != 0 or gaming_box[row][column + 2] != 0 or \
                   gaming_box[row][
                       column + 3] != 0 or gaming_box[row][column + 4] != 0:
               if gaming_box[row][column] == 0:
                   while gaming_box[row][column] == 0:
                       gaming_box[row][column] = gaming_box[row][column + 1]
                       gaming_box[row][column + 1] = gaming_box[row][column + 2]
                       gaming_box[row][column + 2] = gaming_box[row][column + 3]
                       gaming_box[row][column + 3] = gaming_box[row][column + 4]
                       gaming_box[row][column + 4] = 0
               if gaming_box[row][column + 1] == 0 and (
                       gaming_box[row][column + 2] != 0 or gaming_box[row][column + 3] != 0 or gaming_box[row][
                   column + 4] != 0):
                   while gaming_box[row][column + 1] == 0:
                       gaming_box[row][column + 1] = gaming_box[row][column + 2]
                       gaming_box[row][column + 2] = gaming_box[row][column + 3]
                       gaming_box[row][column + 3] = gaming_box[row][column + 4]
                       gaming_box[row][column + 4] = 0
               if gaming_box[row][column + 2] == 0 and (
                       gaming_box[row][column + 3] != 0 or gaming_box[row][column + 4] != 0):
                   while gaming_box[row][column + 2] == 0:
                       gaming_box[row][column + 2] = gaming_box[row][column + 3]
                       gaming_box[row][column + 3] = gaming_box[row][column + 4]
                       gaming_box[row][column + 4] = 0
               if gaming_box[row][column + 3] == 0 and (gaming_box[row][column + 4] != 0):
                   while gaming_box[row][column + 3] == 0:
                       gaming_box[row][column + 3] = gaming_box[row][column + 4]
                       gaming_box[row][column + 4] = 0
       column = 0
       for row in range(0, 5):
           if gaming_box[row][column] == gaming_box[row][column + 1]:
               gaming_box[row][column] = gaming_box[row][column] + gaming_box[row][column + 1]
               gaming_box[row][column + 1] = gaming_box[row][column + 2]
               gaming_box[row][column + 2] = gaming_box[row][column + 3]
               gaming_box[row][column + 3] = gaming_box[row][column + 4]
               gaming_box[row][column + 4] = 0
           if gaming_box[row][column + 1] == gaming_box[row][column + 2]:
               gaming_box[row][column + 1] = gaming_box[row][column + 1] + gaming_box[row][column + 2]
               gaming_box[row][column + 2] = gaming_box[row][column + 3]
               gaming_box[row][column + 3] = gaming_box[row][column + 4]
               gaming_box[row][column + 4] = 0
           if gaming_box[row][column + 2] == gaming_box[row][column + 3]:
               gaming_box[row][column + 2] = gaming_box[row][column + 2] + gaming_box[row][column + 3]
               gaming_box[row][column + 3] = gaming_box[row][column + 4]
               gaming_box[row][column + 4] = 0
           if gaming_box[row][column + 3] == gaming_box[row][column + 4]:
               gaming_box[row][column + 3] = gaming_box[row][column + 3] + gaming_box[row][column + 4]
               gaming_box[row][column + 4] = 0
   elif choice == "k":#this code is for right movement
       column = 0
       for row in range(0, 5):
           if gaming_box[row][column] != 0 or gaming_box[row][column + 1] != 0 or gaming_box[row][column + 2] != 0 or \
                   gaming_box[row][column + 3] != 0 or gaming_box[row][column + 4] != 0:
               if gaming_box[row][column + 4] == 0:
                   while gaming_box[row][column + 4] == 0:
                       gaming_box[row][column + 4] = gaming_box[row][column + 3]
                       gaming_box[row][column + 3] = gaming_box[row][column + 2]
                       gaming_box[row][column + 2] = gaming_box[row][column + 1]
                       gaming_box[row][column + 1] = gaming_box[row][column]
                       gaming_box[row][column] = 0
               if gaming_box[row][column + 3] == 0 and (
                       gaming_box[row][column + 2] != 0 or gaming_box[row][column + 1] != 0 or gaming_box[row][
                   column] != 0):
                   while gaming_box[row][column + 3] == 0:
                       gaming_box[row][column + 3] = gaming_box[row][column + 2]
                       gaming_box[row][column + 2] = gaming_box[row][column + 1]
                       gaming_box[row][column + 1] = gaming_box[row][column]
                       gaming_box[row][column] = 0
               if gaming_box[row][column + 2] == 0 and (
                       gaming_box[row][column + 1] != 0 or gaming_box[row][column] != 0):
                   while gaming_box[row][column + 2] == 0:
                       gaming_box[row][column + 2] = gaming_box[row][column + 1]
                       gaming_box[row][column + 1] = gaming_box[row][column]
                       gaming_box[row][column] = 0

               if gaming_box[row][column + 1] == 0 and gaming_box[row][column] != 0:
                   while gaming_box[row][column + 1] == 0:
                       gaming_box[row][column + 1] = gaming_box[row][column]
                       gaming_box[row][column] = 0
       column = 0
       for row in range(0, 5):
           if gaming_box[row][column + 4] == gaming_box[row][column + 3]:
               gaming_box[row][column + 4] = gaming_box[row][column + 4] + gaming_box[row][column + 3]
               gaming_box[row][column + 3] = gaming_box[row][column + 2]
               gaming_box[row][column + 2] = gaming_box[row][column + 1]
               gaming_box[row][column + 1] = gaming_box[row][column]
               gaming_box[row][column] = 0

           if gaming_box[row][column + 3] == gaming_box[row][column + 2]:
               gaming_box[row][column + 3] = gaming_box[row][column + 3] + gaming_box[row][column + 2]
               gaming_box[row][column + 2] = gaming_box[row][column + 1]
               gaming_box[row][column + 1] = gaming_box[row][column]
               gaming_box[row][column] = 0
           if gaming_box[row][column + 2] == gaming_box[row][column + 1]:
               gaming_box[row][column + 2] = gaming_box[row][column + 2] + gaming_box[row][column + 1]
               gaming_box[row][column + 1] = gaming_box[row][column]
               gaming_box[row][column] = 0
           if gaming_box[row][column + 1] == gaming_box[row][column]:
               gaming_box[row][column + 1] = gaming_box[row][column + 1] + gaming_box[row][column]
               gaming_box[row][column] = 0


'''This function displays the table in the format given'''


def table(Table):  # error1 appends into a number
   # gaming_box = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
   random_index = [0, 1, 2,
                   3,
                   4]  # to randomly pick an index to put the number 2 or 4 we make a list of avalible indexes in the matrix, then randomly pick two numbers from the list and take them as the index of the number we are putting
   random_numbers = [2, 4]  # in the game we are putting the number 4 or 2 randomly in the matrix
   Table[random.choice(random_index)][random.choice(random_index)] = random.choice(
       random_numbers)  # the random.choice method randomly picks a number from the list

   for i in range(5):
       print(" <<_________|_________|_________|_________|___________>>")
       for j in range(5):
           print("  |", format(Table[i][j], "5d"),
                 end=' ')  # the format code simply gives spaces between the numbers in the table. if you change 4d to 5d the numbers will be further apart
       print("  |")
   print(" >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
   print("         ***************ENJOY IT******************    ")


'''this function is used to check whether you are winner or loser '''


def main():
   print("   xxxxxxxxPLAYxxxxxxx2048xxxxxxxGAMExxxxxxxxxHERExxxxxx")
   Table = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]  # first all the numbers in a given matrix are zero
   while True:
       table(Table)

       print("This is python 2048 GAME......")
       Choice = input("please CHOOSE (i) for upward direction,(m) for downwards, (j) for left and (k) for Right ")
       moving_positions(Table, Choice)
       zerorow = []  # Here we create two empty lists this are used to find the indexes of the number zero in the matrix
       zerocolumn = []
       count = 0
       for i in range(0, 5):
           for j in range(0, 5):
               if Table[i][j] == 0:
                   count += 1
                   zerorow.append(i)  # append the i index of the zero value to a zerorow
                   zerocolumn.append(j)  # append the j index of the zero value to a listoforj
       if count > 0:  # meaning if there are zeros in the matrix
           if count > 1:  # if there are two or more zeros
               randomindex = zerorow.index(random.choice(zerorow))
               Table[zerorow[randomindex]][zerocolumn[randomindex]] = 2
           else:
               Table[zerorow[0]][zerocolumn[0]] = 2
       else:
           print("Game over")
           break

       for i in range(0, 5):
           for j in range(0, 5):
               if Table[i][j] == 2048:
                   print("Congartulations YOu won!!!")
                   break


main()

