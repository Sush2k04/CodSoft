def add(a,c):
    return a+c
def mul(a,c):
    return a*c
def div(a,c):
    return a/c
def sub(a,c):
    return a-c
print("=========================================")
print("CALCULATOR")
print("=========================================")

choice=0
while choice!=1:
    
    a=int(input("ENTER A NUMBER:"))
    b=input("ENTER AN OPERATION(+,-,x,/):")
    c=int(input("ENTER ANOTHER NUMBER:"))
    if b=='+':
        print(add(a,c))
    elif b=='-':
        print(sub(a,c))
    elif b=='/':
        print(div(a,c))
    elif b=='x':
        print(mul(a,c))
    print("=========================================")
    d=input("AGAIN?(y/n):")
    if d=='y':
        choice=0
    else:
        choice=1
        print("=========================================")


