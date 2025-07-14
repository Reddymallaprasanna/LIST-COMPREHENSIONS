#Nested listcompressions loop within loop in a single  :listcompressions
n=int(input("Enter the table size::"))
table=[[i*j for j in range(1,n+1)] for i in range (1,n+1)]
print("TABLES OF MATCH")
for row in table:
    print(row)