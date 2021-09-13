N = 2000;
m = 5;
n = 8;
vect = horzcat(zeros(1, n), ones(1, m), [2]);
contor = 0;
for(i=1:N)
afisare = vect(randperm(n+m+1));
poz = find(afisare==2);

if(poz > 1 && poz < m+n)
if(afisare(poz-1) == 0 && afisare(poz+1) == 0) 
contor++;
endif;
endif;
endfor;

p = contor/N;
disp(p);