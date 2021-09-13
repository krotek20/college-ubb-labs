m=unifrnd(150,170);
n=500;
s=unifrnd(5,20);

for i=1:n
  x=normrnd(m,s,[1,100]);
  [m1 m2] = abatere_standard(x)
endfor
