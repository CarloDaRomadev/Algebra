def euclide(x,y)->int:
    if x%y==0:
        return y
    else:
        return euclide(y,x%y)

print(euclide(15,12))