'''create a nXn matrix with manual input numbers by input seperated spaces print all the rows in LC only'''
nums=input("Enter 9 numbers exactly:").split()
if len(nums)!=9:
    print("Enter exactly 9 elements")
else:
    numbers=[int(x) for x in nums]
    matrix=[[numbers[i*3+j] for j in range(3)] for i in range(3)]
    transpose=[[matrix[i][j] for i in range(3)] for j in range(3)]
print("MATRIX:")
for r in matrix:
   print(r) 
print("TRANSPOSE MATRIX:")
for r in transpose:
    print(r)