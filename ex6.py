n=int(input("Enter no.of Rows:"))
pattern=[['* ' if i==j or i+j==n-1  else '  'for i in range(n)]for j in range(n)]
for i in pattern:
    print(' '.join(i)) 