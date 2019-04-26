
#-----function definition------#
def collatz(num):
	if num%2==0:
		#num is even, print and return num divided by 2.
		print(num/2)
		return(num/2)

	elif num%2==1:
		#num is odd, print and return 3*num+1
		print(3*num+1)
		return(3*num+1)



#-----start main-------#
while True:
	try:
		userInput=input('Enter number: ')
		break

	except:
		print('Error! Please enter an integer.')
		


while(userInput!=1):
	userInput=collatz(userInput)
	
