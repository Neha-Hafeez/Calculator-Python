print('****CALCULATOR****')
num1 = int(input( 'first number = '))
num2 = int(input('second number ='))
op=input("operator = ")
add = num1+num2
if op == '+':
	add=num1+num2
	print('addition =',add)
elif op == '*':
	multiply=num1*num2
	print('multiplication = ',multiply)
elif op == '-':
	subtract=num1-num2
	print('subtraction  = ',subtract)
elif op == '/':
	divide=num1/num2
	print('division= ',divide)	
else:
	print('invalid character')