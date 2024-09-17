def area_of_shape(l1,l2,S) :
    if S == "Rectangle" :
        area = l1*l2
        return area
    else :
        area = l1*l2*0.5
        return area
s = input()
l1 = int(input("Enter length"))
l2 = int(input("Enter length"))
a = area_of_shape(l1,l2,s)
print(a)