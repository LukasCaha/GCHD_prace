import sys

def hello():
	print("hello world")
		
def min(list):
	min = sys.maxsize
	for index in range(0, len(list)):
		if(list[index]<min):
			min=list[index]
	print(min)
	
def max(list):
	max = -sys.maxsize -1
	for index in range(0, len(list)):
		if(list[index]>max):
			max=list[index]
	print(max)
	
def isPrime(number):
	print(number)
	divisions = 0
	for a in range (1,number+1):
		if(number%a==0):
			divisions=divisions+1
	if(divisions==2):
		print(True)
	else:
		print(False)