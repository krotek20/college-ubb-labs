pkg load statistics;
m = 1000;
k = 100;
p = 0.8;
v = [];

for i = 1:m
  poz = 0;
  for j = 1:k
    N = binornd(1,p);
    if N == 1
      poz = poz + 1;
      if poz >= k
          poz = 0;
      endif 
    else
      poz = poz - 1;
      if poz < 0
          poz = k - 1;
      endif 
    endif
  endfor
  v = [poz, v];
endfor

clf; grid on; hold on;
N=histc(v, 0:k);
bar(0:k, N, 'hist', 'FaceColor', 'b');