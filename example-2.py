rows=int(input("Enter no.of Rows:"))
pattern=[' '.join([str(num) for num in range(1,i+1)]) for i in range(1,rows+1)]
for line in pattern:
    print(line)




