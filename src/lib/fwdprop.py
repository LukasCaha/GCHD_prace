import random
import math

def sumLayer(input,weights,outneurons):
	output = []
	for outneuron in range(0, outneurons):
			output.insert(outneuron,0)
	for outneuron in range(0, outneurons):
		for inneuron in range(0, len(input)):
			output[outneuron] += input[inneuron]*weights[inneuron*outneurons+outneuron]
	return output

def sigmoid(x):
	return 1/(1+(math.e**-x))

def sigmoidList(list):
	for index in range(0,len(list)):
		list[index] = sigmoid(list[index])
	return list

def randomWeights(length,min,max):
	weights = []
	for i in range(0,length):
		weights.insert(i,random.uniform(min,max))
	return weights

def forwardPropagation(inLayer,compLayer,outLayer,inToCompWeights,compToOutWeights):
	if(len(inToCompWeights) == len(inLayer)*len(compLayer)):
		compLayer = sigmoidList(sumLayer(inLayer,inToCompWeights,len(compLayer)))
	else:
		print("Spatny pocet vah z in to comp1")
		
	if(len(compToOutWeights) == len(compLayer)*len(outLayer)):
		outLayer = sigmoidList(sumLayer(compLayer,compToOutWeights,len(outLayer)))
	else:
		print("Spatny pocet vah z comp1 to out")

	return outLayer
