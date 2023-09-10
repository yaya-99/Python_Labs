a = int(input("Enter a number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b== c :
    print("equilateral triangle.")

elif a > 0 and b > 0 and c> 0:
    if a +b >c and a +c >b and c +b >a :
        print("triangle")
    else :
        print("not forming triangle")
else :
    print("invalid input")
