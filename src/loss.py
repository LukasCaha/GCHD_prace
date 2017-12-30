import basicfunctions as bf

#loss function

def loss(fwdprop,correct):
	return (correct-fwdprop)**2

def lossList(fwdpropList,correctList):
	lost = 0
	min = bf.minLenTwo(fwdpropList,correctList)
	for i in range(0,min):
		lost += loss(fwdpropList[i],correctList[i])
	return lost/min
	
#print(lossList([1,5,5,4,6,8,4,21,3,5],[1,6,4,2,5,10,20
#print(lossList([1,5,5,4,6,8,4,21,3,5],[1,5,5,4,6,8,4,21,3,6]))