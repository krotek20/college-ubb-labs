pkg load statistics;
N = 100;
x = [1 2 3 4];
p = [0/100, 46/100 40/100 10/100 4/100];
v = [];

for i = 1:N
   y = rand();
   contor = 1;
   pContor = p(contor);
   while y > pContor
     contor = contor + 1;
     pContor = pContor + p(contor);
   endwhile
   v = [contor v];
endfor

clf; grid on; hold on;
Hist=histc(v,min(v):max(v));
bar(min(v):max(v),Hist/N,'hist','FaceColor','b');