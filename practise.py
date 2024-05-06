import math as m
a=2
b=3
ans=a**b
print(ans)
c=10.6
print(m.floor(c))
print(m.ceil(c))
#To print Arshad Rocks Rocks Rocks Rocks 5 times
i=1
while i<=5:
    print("Arshad",end=" ")
    i+=1
    j=1
    while j<=4:
        print("Rocks",end=" ")
        j+=1
    print()
#Stock
stock=6
i=1
while i<=6:
    if i>6:
        break
    else:
        print(i,":Candy")
        i+=1
#return Statement
def add_sub(x,y):
    return x+y,x-y #returning multiple values in a statement
add,sub=add_sub(10,5)
print(add,"\n",sub)