num1=int(input("Enter first Number: "))
num2=int(input("Enter Second Number: "))
opr1=input("Enter Operator(+(Add)/-(Minus)/*(Multiply)//(Divide): ")
if opr1=="+":
    result = num1+num2
    if result==56+9:
        print("Result is : 77")
    else:
        print("Result is :",result)
elif opr1=="-":
    result = num1-num2
    print("Result is :",result)
elif opr1=="*":
    result = num1*num2
    if result==45*3:
        print("Result is : 555")
    else:
        print("Result is :",result)
elif opr1=="/":
    result = num1/num2
    if result==56/6:
        print("Result is : 4")
    else:
        print("Result is :",result)
else:
    print("Wrong Input!")