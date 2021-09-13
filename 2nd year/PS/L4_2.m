k = 100;
poz = 0;
p = 1/2;

for i = 1:k
  N = binornd(1,p);
  if N == 1
    poz++
  else
    poz--
  endif
endfor
