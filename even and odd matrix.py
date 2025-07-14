n=int(input("Enter the range:"))
print("Enter",n*n,"Numbers")
num=[int(x) for x in input("Enter numbers:").split()[:n*n]]
matrix=[[num[i*n+j] for j in range(n)] for i in range(n)]
print("MATRIX::")
for k in matrix:
    print(k)
print("1:odd,0:even MATRIX::")
sqmatrix=[[0 if num[i*n+j] %2==0  else 1 for j in range(n)] for i in range(n)]
for s in sqmatrix:
    print(s)