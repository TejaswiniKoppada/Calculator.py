def add(num1,num2):
    return(num1+num2)

def sub(num1,num2):
    return(num1-num2)

def mul(num1,num2):
    return(num1*num2)

def div(num1,num2):
    return(num1/num2)

def loga(num1,num2):
    import math
    return(math.log(num1,num2))

def powr(num1,num2):
    import math
    return(math.pow(num1,num2))

def mod(num1,num2):
    return(num1%num2)

print("Select the operation:")
print("1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Logarithm \n6.Power \n7.Modulo-division")
n=int(input("Enter the operation number:"))

a=int(input("Enter value1:"))
b=int(input("Enter value2:"))

if(n==1):
    print("Addition of",a,"and",b,"is",add(a,b))
elif(n==2):
    print("Subtraction of",a,"and",b,"is",sub(a,b))
elif(n==3):
    print("Multiplication of",a,"and",b,"is",mul(a,b))
elif(n==4):
    print("Division of",a,"and",b,"is",div(a,b))
elif(n==5):
    print("log(",a,",",b,")is",loga(a,b))
elif(n==6):
    print("Power(",a,",",b,")is",powr(a,b))
elif(n==7):
    print("Remainder of",a,"and",b,"is",mod(a,b))