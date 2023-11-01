x = 13
b = 6

if x == b:
    print("bad")
else:
    print("good")

    # the above condition is a condition that evaluate wheter it is true or false
    
if x == b:
    print("bad")
elif x > b:
    print("good")
else:
    print("badder")


y =  int(input("Enter your Number "))

if y <= 100 and x>0:
    if y >= 86:
        print("A")
    elif y >= 85:
        print("B")
    elif y >= 75:
        print("C")
    elif y >= 55:
        print("D")
    elif y >= 40:
        print("E")
    elif y <= 39:
        print("F")        
    else:
        print("Invalid number")