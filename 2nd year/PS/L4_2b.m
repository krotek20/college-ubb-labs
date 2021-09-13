k = 100;

p = 1/2;

m = 100;
v = [zeros(1,m)];

pasi = 0;

for j = 1:m
  ok = 0;
  poz = 0;
  for i = 1:k
    N = binornd(1,p);
    if N == 1
      poz++;
    else
      poz--;
      if ok == 0
        ok = 1;
        pasi = pasi + i;
      endif
    endif
  endfor
  v(j) = poz;
endfor
pasi = pasi/m


N=histc(v,-100:100);
bar(-100:100,N/m,'hist','FaceColor','c');