% 1.d.

function [m1 m2] = proportie()
  n=2000;
  p=binornd(1,0.5,1,n);
  a=0.01;
  
  x=mean(p);
  z=norminv(1-a/2,0,1);
  
  m1=max([x-sqrt((x*(1-x))/n)*z,0]);
  m2=min([x+sqrt((x*(1-x))/n)*z,1]);
  
  if nargout < 1
     m1 = [m1; m2];
  end
endfunction
