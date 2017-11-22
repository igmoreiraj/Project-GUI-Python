import time
import random

import Calculator

loopMax=random.randint(10,30)

#Print mathing
print("Request for " + str(loopMax) + " maths received... Beginning mathing sequence...")


#Create list
operations=['+']
#Use append function to add to the list
operations.append('-')
operations.append('+')
operations.append('*')

#print operations lenghts
print("Operation count "+ str(len(operations))

#Take a peek at what is in the list
print("Computer will calculate using the following operations " + str(operations))
#Add 3 lines
print('\n\n')
#Loop- start list index is 0 not 1
for i in range(loopMax):
	num1=random.randint(-99,99)
	num2=random.randint(-99,99)
	
	print("Mathing with " + str(num1) + "and " + str(num2))
	
	#Generate random sleeptime between 0 and 1
	#sleeptime=random.randint(0,1)
	sleeptime=0
	print('IN FOR LOOP:')
	for operation in range(operations):
		print('operation = ' + operation)
		calculator.runOperation(operation,num1,num2)
		print()
		
	print('\n')
	print('INDEX FOR LOOP')
	
	for i in range(len(operations)):
		print('i = ' +str(i))
		
		print('operation = ' + operations[i])
		calculator.runOperation(operations[i],num1,num2)
		print()
		
		
	time.sleep(sleeptime)
	print('\n-----------------\n')
	
	print('Done mathing...Goodbye!')
	time.sleep(2)
	
	
	
	
	
	
	
	
	








