I=imread("image15.jpg") 
imshow(I) 
[x,y]=ginput(2) 
z=1023.6; 
fy=1178.6; 
fx=1170.1; 
x1=z*(x(1)/fx); 
x2=z*(x(2)/fx); 
y1=z*(y(1)/fy); 
y2=z*(y(2)/fy); 
dist=sqrt((y2-y1)^2+(x2-x1)^2); 
fprintf('The distance is %.02f mm',dist); 
