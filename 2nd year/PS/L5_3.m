pkg load statistics;
N = 1000;
U1=rand(1,N);
U2=rand(1,N);

R=sqrt(-2*log(U1));
V=2*pi*U2;
X=R.*cos(V);
Y=R.*sin(V);

rez = find(sqrt(X.^2+Y.^2) < 0.5);
length(rez) / N
1-exp(-1/8)