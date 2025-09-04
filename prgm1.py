n=int(input("Enter the Number: "))

maxPrime = -1

while n%2== 0:          # LOOP FOR ALL EVEN NUMBERS
    maxPrime = n
    n=n//2         # using single slash would give float value, so using double slash to get integer value

print("N: ", n)    # to check the value of n after removing all 2s

for i in range(3, int(n**0.5)+1, 2):     # LOOP FOR ALL ODD NUMBERS
    while n%i==0:
        maxPrime = i
        n = n/i

if n>2:
    maxPrime=n

print("Max Prime factor: ",int (maxPrime))
