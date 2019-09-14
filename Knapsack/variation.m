function v = variation(cross,p)

%cross:需要变异的数据，p：变异概率，v:变异生成的新数据
v=[];
vL = 1;
v1 = rand(size(cross,1),size(cross(),2));
for i = 1 : size(cross,1),
	findVar = find(v1(i,:)<p);
	if length(findVar)==0,continue;
	end 
	v(vL,:) = cross(i,:);
	for j = 1 : length(findVar),
		v(vL,findVar(j)) = xor(v(vL,findVar(j)),1);
	end
	vL++;
end
