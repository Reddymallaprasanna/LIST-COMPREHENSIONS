'''list compreshion .......input version 
x=[1,2,3,4,5]
for i in range(11):
    print(i,end=' ')
'''

#stepby-step input of lc
x=int(input("Enter the range:"))
nums=[int(input(f"Enter a number:{i+1}:")) for i in range(x)]
print(nums)
