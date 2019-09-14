function result = operation(X)


X1 = -3.0+(12.1+3.0)*bin2dec(num2str(X(:,1:18)))/(2^18-1);
X2 = 4.1+(5.8-4.1)*bin2dec(num2str(X(:,19:33)))/(2^15-1);
result = 21.5+X1.*sin(4*pi.*X1)+X2.*sin(20*pi.*X2);


end