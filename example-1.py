rows=int(input("Enter no.of Rows:"))
pattern=[' '.join(['*' for _ in range(i)]) for i in range(1,rows+1)]
for line in pattern:
    print(line)