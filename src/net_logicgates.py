#neural net data
from lib import fwdprop as fp
from lib import loss as l
from lib import basicfunctions as bf

import random as r
import matplotlib.pyplot as plt


#net settings
learnRate = 0.01
batch = 1
#layers
inLayer = [0,0]
compLayer = [0,0,0,0]
outLayer = [0]
#weights
min = -1
max = 1
inToCompWeights = fp.randomWeights(len(inLayer)*len(compLayer),min,max)
desiredInComp = []
for d in range(0,len(inLayer)*len(compLayer)):
	desiredInComp.insert(d,0)
compToOutWeights = fp.randomWeights(len(compLayer)*len(outLayer),min,max)
desiredCompOut = []
for d in range(0,len(compLayer)*len(outLayer)):
	desiredCompOut.insert(d,0)
#statistic data
lost = 100
out = []
cor = []
lostStats = []
#data
d=3
if(d==0):
	#XOR
	inLayer1 = [1,1,0,0]
	inLayer2 = [1,0,1,0]
	outLayer1 = [0,1,1,0]
if(d==1):
	#OR
	inLayer1 = [1,1,0,0]
	inLayer2 = [1,0,1,0]
	outLayer1 = [1,1,1,0]
if(d==2):
	#AND
	inLayer1 = [1,1,0,0]
	inLayer2 = [1,0,1,0]
	outLayer1 = [1,0,0,0]
if(d==3):
	#random
	inLayer1 = [1,1,0,0]
	inLayer2 = [1,0,1,0]
	outLayer1 = [1,0,0,0]
	
dataLen = bf.minLenThree(inLayer1,inLayer2,outLayer1)

for counter in range (0,100):
	for d in range(0,len(inLayer)*len(compLayer)):
		desiredInComp[d] = 0
	for d in range(0,len(compLayer)*len(outLayer)):
		desiredCompOut[d] = 0
	#fwdprop
	rnd = counter%dataLen-1 #r.randint(0,dataLen-1)
	inLayer = [inLayer1[rnd],inLayer2[rnd]]
	cor.insert(counter, outLayer1[rnd])
	out.insert(counter, fp.forwardPropagation(inLayer,compLayer,outLayer,inToCompWeights,compToOutWeights)[0])
	#loss
	lostStats.insert(counter,l.lossList(out,cor))
	#print(l.lossList(out,cor))
	#backprop
	for d in range(0,len(compLayer)*len(outLayer)):
		desiredCompOut[d] += (outLayer[0] - outLayer1[rnd]) * outLayer[0] * (1-outLayer[0])
	for i in range(0,len(inLayer)):
		for c in range(0,len(compLayer)):
		#desiredInComp[i*len(compLayer)+o] -= (compLayer[o] - (compLayer[o]+desiredCompOut[o])) #* inToCompWeights[i*len(compLayer)+o]
			for o in range(0,len(outLayer)):
				desiredInComp[i*len(compLayer)+c] += desiredCompOut[c]*compToOutWeights[c]*(1-compLayer[c])*compLayer[c] #* inToCompWeights[i*len(compLayer)+o]
	if(counter%batch==0):
		for d in range(0,len(compLayer)*len(outLayer)):
			compToOutWeights[d] += desiredCompOut[d] * learnRate/(counter+1) * compLayer[d]/ batch
			if(compToOutWeights[d]>max):
				compToOutWeights[d] = max 
			if(compToOutWeights[d]<min):
				compToOutWeights[d] = min 
		for d in range(0,len(inLayer)*len(compLayer)):
			inToCompWeights[d] += desiredInComp[d]* learnRate/(counter+1) * inLayer[d % len(inLayer)]/ batch
			if(inToCompWeights[d]>max):
				inToCompWeights[d] = max 
			if(inToCompWeights[d]<min):
				inToCompWeights[d] = min 
			
plt.plot(lostStats)
plt.show()
	
print(inToCompWeights)
print(compToOutWeights)