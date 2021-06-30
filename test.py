def pascal_triangle(num):
    pascal_list = [] #Creating a general list that'll hold the pascal numbers as a list
    for row in range(num+1): #This for loop is to create each ROW
        for space in range(num-row): #This for loop is to Create spaces before printing the first number
            print(format(' ', '<2'), end='')
        temp_list = [] #This is an inner list holding each row of the pascal triangle
        for col in range(row+1): #This for loop is to create each COLUMN
            if (row + col == row) or (row+col == 2*row): #This condition is for the first and last numbers in a ROW
                temp_list.append(1)
                print(format(1, '<2'), end='  ')
            else: #For every other number in a ROW other than the first and last numbers
                first_num = pascal_list[row-1][col-1]
                second_num = pascal_list[row-1][col]
                answer = first_num + second_num
                temp_list.append(answer)
                print(format(answer, '<3'), end=' ')
        pascal_list.append(temp_list) #This is the main list holding every progressive number of the pascal triangle
        print() #For new line after each row...

pascal_triangle(8)


