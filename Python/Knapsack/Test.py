#创建（10*10）随机01数组
import numpy as np

X = np.rint(np.random.rand(10,15))
goods = np.array([[66,65,63,60,58,56,50,30,20,15,10,8,5,3,1],[65,20,25,30,10,20,25,15,10,10,10,4,4,2,1]],dtype="f")
goods = np.append(goods,(goods[0]/goods[1]).reshape(1,np.size(X,1)),axis=0)

#运算背包值
def operation(X):
	result = np.dot(X,goods.T)
	return result


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
lunpan_result = np.zeros(np.size(X,0))


np.argwhere(lunpan>np.random.rand())[0,0]