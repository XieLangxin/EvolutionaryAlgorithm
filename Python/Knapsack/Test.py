#创建（10*10）随机01数组

X = np.rint(np.random.rand(10,15))
goods = array([[66,65,63,60,58,56,50,30,20,15,10,8,5,3,1],[65,20,25,30,10,20,25,15,10,10,10,4,4,2,1]],dtype="f")
np.append(goods,(goods[0]/goods[1]).reshape(1,size(X,1)),axis=0)

#计算适应度函数
values = operation(X);
p = values/sum(values);

#计算轮盘赌概率
lunpan = 
count = 0
for i in range(9):
	count += p[:,0][i,0]
	print count
	lunpan.append(count)



#运算背包值
def operation(X):
	result = np.dot(X,goods.T)
	return result

