hold on
a=-2; b=2;

g=@(x) exp(-x.^2);

M=max(g([a:0.01:b]))
x=[unifrnd(a,b,1,30)];
y=[unifrnd(0,M,1,30)];

plot(x,y,'r*')

v=[rand(1,n)]*4-2;
v=sort(v);

plot(a:0.01:b, g([a:0.01:b]))

f=mean(y<g(x))
aprox1=f*(b-a)*M
aprox2=(b-a)/30*sum(g(x))
integral(g,a,b)