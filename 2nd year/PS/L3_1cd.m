v = [1 1 1 1 1 2 2 2 3 3];
a=0;
b=0;
for i=1:5000
  bila = randsample(v,3);
  
  if(bila(1)==1 || bila(2)==1 || bila(3)==1)
  a=a+1;
    if(bila(1)==bila(2)&&bila(2)==bila(3))
      b=b+1;
    endif
  endif

end

b/a

#5/10 * 4/9 * 3/8= 1/12 
# C(5,3) = 4*5/2=10
# C(10,3) =8*9*10/2*3 = 4*3*10=120
# P(A)= 11/12
#(1/12) / (11/12) = 1/11