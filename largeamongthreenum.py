num1=int(input("num1="))
num2=int(input("num2="))
num3=int(input("num3="))
if num1>num3 and num1>=num3:
     maximum=num1
elif num2>num1 and num2>num3:
    maximum=num2
elif num3>num1 and num3>=num2:
    maximum=num3
    print(maximum,"largest num")
