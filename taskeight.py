sumOfBoth=0
sumOfFour=0
sumOfEight = 0
firstmultiple =1
for number in range(5):
	count = 4
	firstmultiple *= count
	sumOfFour += firstmultiple                 
	
	
secondmultiple =1
for number in range(5):
	count = 8
	secondmultiple *= count
	sumOfEight += secondmultiple
	
sumOfBoth= sumOfFour  +	sumOfEight
print(sumOfBoth)
