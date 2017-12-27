#neural net data
import fwdprop as fp
import loss as l
import random as r
import basicfunctions as bf

#layers
inLayer = [0,0]
compLayer = [0,0,0,0]
outLayer = [0]
#weights
min = -5
max = 5
inToCompWeights = fp.randomWeights(len(inLayer)*len(compLayer),min,max)
compToOutWeights = fp.randomWeights(len(compLayer)*len(outLayer),min,max)
#statistic data
lost = 100
out = []
cor = []
#data
d=0
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
	
dataLen = bf.minLenThree(inLayer1,inLayer2,outLayer1)

for counter in range (0,100):
	#fwdprop
	rnd = r.randint(0,dataLen-1)
	inLayer = [inLayer1[rnd],inLayer2[rnd]]
	cor.insert(counter, outLayer1[rnd])
	out.insert(counter, fp.forwardPropagation(inLayer,compLayer,outLayer,inToCompWeights,compToOutWeights)[0])
	#loss
	print(l.lossList(out,cor))
	#backprop
