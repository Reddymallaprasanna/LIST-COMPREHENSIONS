n=int(input("Enter the range:"))
print("Enter",n*n,"Numbers")
num=[int(x) for x in input("Enter numbers:").split()[:n*n]]
matrix=[[num[i*n+j] for j in range(n)] for i in range(n)]
print("MATRIX::")
for k in matrix:
    print(k)
print("PRIME NUMBER MATRIX::")
sqmatrix=[[num[i*n+j] if num[i*n+j] %2==0 else 0  for j in range(n)] for i in range(n)]
for s in sqmatrix:
    print(s)