n=int(input("Enter number of series: "))
fiblist = [0,1]

for i in range(0, n):
    fiblist.append(fiblist[i] + fiblist[i+1])

print("Series are", fiblist)


gratio=[fiblist[i]/float(fiblist[i-1]) for i in range(2,len(fiblist))]
print("Golden ratio: ", gratio)

# ALSO FIBONACCI SERIES CAN BE WRITTEN USING WHILE LOOP

'''

n=int(input("Enter number of series: "))
a,b=0,1
while a<=n:
    print(a, end=" ")
    a,b=b,a+b

'''