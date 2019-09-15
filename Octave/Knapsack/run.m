function X = run(X)
	global max_capacity;%最大容量
	global n;%总个数
	global rate_mutation;
	global rate_crossover;
	%计算值
	values = operation(X)(:,1);
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
	for i = 1 : size(X,1),
		lunpan_result(length(lunpan_result)+1) = find(lunpan>=rand())(1:1);
	end

	%交叉
	cross=[];
	crossLength = 0;
	for i = 1 : (size(X,1)/2),
		if rand()>=rate_crossover,continue;
		end;
		if lunpan_result(i*2-1)==lunpan_result(i*2),continue;
		end;
		cross1 = floor(rand()*(n-2))+1;
		cross2 = floor(rand().*(n-1-cross1))+cross1+1;
		cross(++crossLength,:) = [X(lunpan_result(i*2-1),1:cross1) X(lunpan_result(i*2),cross1+1:cross2) X(lunpan_result(i*2-1),cross2+1:n)];
		cross(++crossLength,:) = [X(lunpan_result(i*2),1:cross1) X(lunpan_result(i*2-1),cross1+1:cross2) X(lunpan_result(i*2),cross2+1:n)];
	end
	%变异
	v=variation([X;cross],rate_mutation);
	Y = [X;cross;v];
	Y = correct(Y);
	values = operation(Y);
	Z = [values(:,2) Y];
	[~,index]=sort(Z(:,1));
	Z=flipud(Z(index,:));
	X = Z(1:size(X,1),2:n+1);
	operation(X(1,:))
end