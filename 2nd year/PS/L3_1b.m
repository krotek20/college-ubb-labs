v = [1 1 1 1 1 2 2 2 3 3];
k=0;
for i=1:5000
  bila = randsample(v,3);
  
  if(bila(1)==1 && bila(2)==1 && bila(3)==1)
  k=k+1;
  endif
end
k/5000