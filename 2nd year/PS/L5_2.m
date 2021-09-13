pkg load statistics;
lambda = 1/12;
N = 1000;
v = [];

for i = 1:N
  p = rand();
  u = -1/lambda*log(1-x);
  v = [u v];
endfor

v