n=1000;
x=zeros(1,n);
m=165;
sigma=10;

for i=1:n
    d=normrnd(m,sigma);
    x(i)=d;
endfor

g=(max(x)-min(x))/10;
%hist(x,10,1/g)
hold on

v=[min(x):0.01:max(x)];
N=normpdf(v,m,sigma);
%plot(v,N)

mean(x)
std(x)
k=0;
for i=1:n
  if(x(i) >= 160 && x(i) <= 170)
    k=k+1;
  endif
endfor
k/n

real = normcdf(170,m,sigma) - normcdf(160,m,sigma);
real