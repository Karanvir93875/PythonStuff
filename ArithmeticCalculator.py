print('*****Karanvirs first calculator*****')
tool=input ('Press any key if you wish to use this calculator')
tool=input ('Please select an operation (+,-,/,*) : ')
print('You have chosen: ', tool)
num1=int(input("Please enter you first number: "))
num2=int(input("Please enter your second number: ")) 

if tool == '+':
	print("You have chosen addition, thus your answer is: ", num1+num2,", Calc-you-later!")
	
elif tool == '-':
		print("You have chosen subtraction, thus your answer is: ", num1-num2,", Calc-you-later!")
		
elif tool == '*':
		print("You have chosen multiplication, thus your answer is: ", num1*num2,", Calc-you-later!")
		
elif tool == '/':
		print("You have chosen division, thus your answer is: ", num1/num2, ", Calc-you-later!")
		
else:
	print("You have done something wrong!") 
