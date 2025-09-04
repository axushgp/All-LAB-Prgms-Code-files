#declare a value of acceleration a=-16
a=-16
b=int(input ("Enter the velocity : "))
pHeight=float (input ("Enter player height : "))

t=float(-b/a)
print ("Time : ",t," seconds")

h= 0.5*(a*(t**2)) + (b*t)
print ("Height is : " ,h, " feet")

h=h+pHeight
print ("Total Height is : ",h," feet")
