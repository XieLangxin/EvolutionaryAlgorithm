function result = operation(X)


 X1 =-2.048+4.096*bin2dec(num2str(X(:,1:3)))/(2^3-1);
X2 =-2.048+4.096*bin2dec(num2str(X(:,4:6)))/(2^3-1);
result = 100*(X2-X1.*X1).*(X2-X1.*X1)+(1-X1).*(1-X1);

end