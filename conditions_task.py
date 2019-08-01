print("Welcome to the Python Calculator:\n")
num1=float(input("	Enter the first number: "))
num2=float(input("	Enter the second number: "))
oper=input("	Choose the operation (+, -, /, *): ")
if oper=="+":
	num3=num1+num2
	print("	The answer is %s." % (num3))
elif oper=="-":
	num3=num1-num2
	print("	The answer is %s." % (num3))
elif oper=="/":
	num3=num1/num2
	print("	The answer is %s." % (num3))
elif oper=="*":
	num3=num1*num2
	print("	The answer is %s." % (num3))
else:
	print("	Error you have not inputted an operator from the list given, please try again.")