#!/usr/bin/env python3
#创建（10*10）随机01数组
import numpy as np

X = np.array(np.rint(np.random.rand(10,50)),dtype='i')
goods = np.array([[220,208,198,192,180,180,165,162,160,158,155,130,125,122,120,118,115,110,105,101,100,100,98,96,95,90,88,82,80,77,75,73,72,70,69,66,65,63,60,58,56,50,30,20,15,10,8,5,3,1],[80,82,85,70,72,70,66,50,55,25,50,55,40,48,50,32,22,60,30,32,40,38,35,32,25,28,30,22,50,30,45,30,60,50,20,65,20,25,30,10,20,25,15,10,10,10,4,4,2,1]],dtype="f")
goods = np.append(goods,(goods[0]/goods[1]).reshape(1,np.size(X,1)),axis=0)
goods = goods.T[np.lexsort(-goods)].T
#运算背包值
def operation(X):
	result = np.dot(X,goods.T)
	return result
#给矩阵添加一行
def addLine(M,l):
	if np.size(M)==0:
		M=np.append(M,l,axis=1)
	else:
		M=np.append(M,l,axis=0)
	return M
def run(X,aa,bb):
	#计算适应度函数
	values = operation(X)[0:np.size(X,1),0]
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
		if np.random.rand()>aa:
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
		findVar = np.argwhere(v1[i]<bb)
		if np.size(findVar)==0:
			continue
		line = cross[i].copy()
		for j in range(np.size(findVar)):
			line[findVar[j]]= line[findVar[j]]^1
		v = addLine(v,line.reshape(1,np.size(X,1)))
			
	#校正

	Y = np.array(X.copy(),dtype='i')
	if np.size(cross)!=0:
		Y = np.append(Y,cross,axis=0)
	if np.size(v)!=0:
		Y = np.append(Y,v,axis=0)
	for i in range(np.size(Y,0)):
		count = 0;
		for j in range(np.size(Y,1)):
			if count+Y[i][j]*goods[1][j]<=1000:
				count+=Y[i][j]*goods[1][j]
			else:
				Y[i,j:np.size(Y,1)]=0
				break
	values = operation(Y)[0:np.size(Y,0),0:1]
	Y = np.append(values,Y,axis=1)
	Y = Y[np.lexsort(-Y[:,::-1].T)][:,1:np.size(Y)]
	X = np.array(Y[0:np.size(X,0),:],dtype="i")
	return X;
for i in range(1000):
	X = run(X,0.6,0.1)
	print(operation(X))	
	if operation(X)[0][0]==3103:
		print(i)
		break
