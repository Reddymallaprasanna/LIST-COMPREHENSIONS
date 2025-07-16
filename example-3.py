rows=int(input("Enter no.of Rows:"))
pattern=[' '.join([chr(97+j) for j in range(i)]) for i in range(1,rows+1)]
for line in pattern:
    print(line)




