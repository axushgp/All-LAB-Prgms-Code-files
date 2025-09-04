a=-16
b=int(input ("Enter the velocity : "))
pHeight=float (input ("Enter player height : "))

t=float(-b/(2*a))
print ("Time : ",t," seconds")

h= (a*(t**2)) + (b*t)
print ("Height is : " ,h, " feet")

h=h+pHeight
print ("Total Height is : ",h," feet")