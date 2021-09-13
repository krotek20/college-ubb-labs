v = 0;
m = 100;
#probabilitatea ca un bilet sa aiba exact doua nr castigatoare
p=sum(hygernd(2:6,49,6)); 

x = [zeros(1,m)]

for i=1:m
  contor = 0;
  v = hygernd(49,6,6);
  while v < 2
    contor = contor+1;
    v = hygernd(49,6,6);
  endwhile
  x = [x contor]
endfor

N=histc(x,0:max(x));
bar(0:max(x),N/m,'hist','FaceColor','b');
bar(0:max(x),geopdf(0:max(x), 6, p),'FaceColor','y');
legend('estimated probabilities','theoretical probabilities');