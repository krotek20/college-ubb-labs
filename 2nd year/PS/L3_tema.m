hold on;
n=5000;
p=1/3;

a=binornd(5,p,1,n)

X=histc(a,0:5);
b1=bar(0:5,X/n,'hist','FaceColor','g');
b2=bar(0:5,binopdf(0:5,5,p),'FaceColor','y');