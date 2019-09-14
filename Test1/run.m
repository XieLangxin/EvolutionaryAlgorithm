function X = run(X)
%数组转十进制

%计算值
values = operation(X);


%计算适应度函数
p = values./sum(values);

%计算轮盘赌概率
lunpan = [];
count = 0;
for i = 1 : length(p),
	count += p(i);
	lunpan(i) = count;
end

%找到轮盘赌随机数字对应元素
lunpan_result = [];
for i = 1 : 10,
	lunpan_result(length(lunpan_result)+1) = find(lunpan>=rand())(1:1);
end

%交叉
cross=[];
crossLength = 0;
for i = 1 : 5,
	if rand()>=0.6,continue;
	end;
	if lunpan_result(i*2-1)==lunpan_result(i*2),continue;
	end;
	cross1 = floor(rand()*31)+1;
	cross2 = floor(rand().*(32-cross1))+cross1+1;
	cross(++crossLength,:) = [X(lunpan_result(i*2-1),1:cross1) X(lunpan_result(i*2),cross1+1:cross2) X(lunpan_result(i*2-1),cross2+1:33)];
	cross(++crossLength,:) = [X(lunpan_result(i*2),1:cross1) X(lunpan_result(i*2-1),cross1+1:cross2) X(lunpan_result(i*2),cross2+1:33)];
end

%变异
v=variation([X;cross]);

Y = [X;cross;v];
values = operation(Y);
Y = [values Y];
[~,index]=sort(Y(:,1));
B=flipud(Y(index,:));
Y = B(1:10,2:34);
X = Y;
a = max(values)
end;