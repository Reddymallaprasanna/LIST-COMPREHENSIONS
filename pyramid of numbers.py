rows=int(input("Enter no.of Rows:"))
pattern=[' ' .join([str(num)for num in range(1,rows-i+1)]) for i in range(rows)]
for line in pattern:
    print(line) 