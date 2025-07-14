'''write a code to consider a LC:
to calculate square of 16 values as nXn matrix and print the list of squares in each row'''
n=int(input("Enter the range:"))
print("Enter",n*n,"Numbers")
num=[int(x) for x in input("Enter numbers:").split()[:n*n]]
matrix=[[num[i*n+j] for j in range(n)] for i in range(n)]
print("MATRIX::")
for k in matrix:
    print(k)
print("SQUARE MATRIX::")
sqmatrix=[[num[i*n+j]**2 for j in range(n)] for i in range(n)]
for s in sqmatrix:
    print(s)
