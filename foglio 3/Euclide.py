def euclide(x,y)->int:
    if x%y==0:
        return y
    else:
        return euclide(y,x%y)

x = input("primo numero:")
y = input("secondo numero:")
print(euclide(int(x),int(y)))