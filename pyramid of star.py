rows=int(input("Enter no.of Rows:"))
pattern=[(' ' * (rows+i) + '*' * (2*i-1)) for i in range(1,rows+1)]
for line in pattern:
    print(line)




