function X = Knapsack()
	clear;
	global max_capacity = 1000;%最大容量
	global n = 50;%总个数
	global rate_mutation = 0.05;
	global rate_crossover = 0.6;
	goods_info = [[220,208,198,192,180,180,165,162,160,158,155,130,125,122,120,118,115,110,105,101,100,100,98,96,95,90,88,82,80,77,75,73,72,70,69,66,65,63,60,58,56,50,30,20,15,10,8,5,3,1];[80,82,85,70,72,70,66,50,55,25,50,55,40,48,50,32,22,60,30,32,40,38,35,32,25,28,30,22,50,30,45,30,60,50,20,65,20,25,30,10,20,25,15,10,10,10,4,4,2,1]];
	density = goods_info(1,:)./goods_info(2,:);
	goods_info = [density;goods_info]';
	[~,index]=sort(goods_info(:,1));
	goods_info=flipud(goods_info(index,:));
	global goods = goods_info';
	X = floor(rand(20,50)*2);
	for i = 1:1000,
		X = run(X);
	end;
	operation(X);
end