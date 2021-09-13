
m = 1000;
k = 0;
v = [zeros(1,m)];
for i=1:m

B1 = binornd(1,0.8);
if B1 == 1
  B2 = binornd(1,0.9);
  else
  B2 = binornd(1,0.6);
endif

if B2 == 1 && B1 == 1
  B3 = binornd(1,0.6);
  elseif B2 == 1 && B1 == 0
  B3 = binornd(1,0.2);
  elseif B2 == 0 && B1 == 1
  B3 = binornd(1,0.9);
  else
  B3 = binornd(1,0.4);
endif
  
if B3 == 1
  B4 = binornd(1,0.3);
  else
  B4 = binornd(1,0.5);
endif

if B3 == 1
  B5 = binornd(1,0.5);
  else
  B5 = binornd(1,0.8);
endif
  
if B4 == 1 && B5 == 1
  B6 = binornd(1,0.5);
  elseif B4 == 0 && B5 == 1
  B6 = binornd(1,0.3);
  elseif B4 == 1 && B5 == 0
  B6 = binornd(1,0.8);
  else
  B6 = binornd(1,0.5);
endif



n = B1*1 + B2*2 + B3*4 + B4*8 + B5*16 + B6*32;
if n == 23
  k++;
endif
v(i) = n;
endfor

k/m

N=histc(v,0:64);
bar(0:64,N/m,'hist','FaceColor','b');