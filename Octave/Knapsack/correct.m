function Y = correct(Y)
	global goods;
	global max_capacity;
	for i = 1:size(Y,1)
		count = 0;
		j;
		for j = 1:size(Y,2)
			if (count+Y(i,j)*goods(3,j))<=max_capacity,
				count += Y(i,j)*goods(3,j);
			else break;
			end;
		end;
		Y(i,j:size(Y,2)) = 0;
	end;
end