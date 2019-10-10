#!/usr/bin/env python3
#coding:utf-8
import numpy as np
import random
np.set_printoptions(threshold=np.inf)
# 导入数组数据
file_objtct = open("gr48.txt")
file_content = file_objtct.read()
file_content = file_content.replace("\r\n","")
B = file_content.split(' ')
count = 0
num_city = 48
locations = np.arange(num_city*num_city).reshape(num_city, num_city)
for i in range(0,num_city):
	for j in range(0,num_city):
		if B[count]!="0":
			locations[i][j]=B[count]
			count+=1
		else:
			locations[i][j]=0
	count+=1
#编码
X = np.array(np.random.rand(10,47),dtype='d')
B = np.arange(2,49)
C = np.arange(2,49)
for i in range(0,np.size(B,0)):
	C[i] = B[np.size(B,0)-i-1]
for i in range(0,np.size(X,0)):
	X[i] = np.multiply(X[i],C)
X = X.astype(np.int)

def operation(X):
	J = np.zeros(np.size(X,0)*48,dtype='i').reshape(np.size(X,0),48)
	for i in range(0,np.size(X,0)):
		for j in range(0,47):
			count = 0
			for k in range(0,48):
				if J[i][k]!=0:
					continue
				if X[i][j]==count:
					J[i][k] = j+1
					break
				else:
					count+=1
	result = np.zeros(np.size(X,0),dtype='f').reshape(np.size(X,0),1)
	for i in range(0,np.size(J,0)):
		for j in range(0,47):
			result[i][0]+=locations[J[i][j]][J[i][j+1]] if (J[i][j]>J[i][j+1]) else locations[J[i][j+1]][J[i][j]]
	return result
def addLine(M,l):
	if np.size(M)==0:
		M=np.append(M,l,axis=1)
	else:
		M=np.append(M,l,axis=0)
	return M
def run(X):
	values = operation(X)
	p = values/sum(values)
	#计算轮盘赌概率
	lunpan = np.zeros(np.size(X,0))
	count = 0
	for i in range(np.size(X,0)):
		count += p[i]
		lunpan[i] = count
	#找到轮盘赌随机数字对应元素
	lunpan_result = np.zeros(np.size(X,0),dtype='i')

	for i in range(np.size(X,0)):
		lunpan_result[i] = np.argwhere(lunpan>np.random.rand())[0,0]
	#交叉
	cross = np.array([[]],dtype='i')
	for i in range(int(np.size(X,0)//2)):
		if np.random.rand()>0.6:
			continue
		if lunpan_result[2*i]==lunpan_result[2*i+1]:
			continue
		cross1 = int(np.floor(np.random.rand()*(np.size(X,0)-2))+1)
		cross2 = int(np.floor(np.random.rand()*(np.size(X,0)-1-cross1))+cross1+1)
		line1 = np.append(X[lunpan_result[2*i],0:cross1],np.append(X[lunpan_result[2*i+1],cross1:cross2],X[lunpan_result[2*i],cross2:np.size(X,1)]))
		line2 = np.append(X[lunpan_result[2*i+1],0:cross1],np.append(X[lunpan_result[2*i],cross1:cross2],X[lunpan_result[2*i+1],cross2:np.size(X,1)]))
		cross = addLine(cross,line1.reshape(1,np.size(X,1)))
		cross = addLine(cross,line2.reshape(1,np.size(X,1)))
	#变异
	v = np.array([[]],dtype='i')
	v1 = np.random.rand(np.size(cross,0),np.size(cross,1))
	for i in range(np.size(v1,0)):
		findVar = np.argwhere(v1[i]<0.05)
		if np.size(findVar)==0:
			continue
		line = cross[i].copy()
		for j in range(np.size(findVar)):
			line[findVar[j]]= random.sample(range(0,48-findVar[j]),1)
		v = addLine(v,line.reshape(1,np.size(X,1)))
	Y = np.array(X.copy(),dtype='i')
	if np.size(cross)!=0:
		Y = np.append(Y,cross,axis=0)
	if np.size(v)!=0:
		Y = np.append(Y,v,axis=0)
	values = operation(Y)
	Y = np.append(values,Y,axis=1)
	Y = Y[np.lexsort(Y[:,::-1].T)][:,1:np.size(Y)]
	X = np.array(Y[0:np.size(X,0),:],dtype="i")
	print(operation(X))
	return X
for i in range(1000):
	X = run(X)
	# print(operation(X))	
	# if operation(X)[0][0]==3103:
	# 	print(i)
	# 	break
# location = 
# locations = random.sample(range(1,49),48)
# print(locations)