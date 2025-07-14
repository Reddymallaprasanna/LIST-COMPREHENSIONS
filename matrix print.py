n=int(input("Enter size:"))
print("Enter",n*n,"Numbers")
num=[int(x) for x in input("Enter numbers:").split()[:n*n]]

matrix=[[num[i*n+j] for j in range(n)] for i in range(n)]
for k in matrix:
    print(k)
flat=[k for r in matrix for k in r]
print(flat)