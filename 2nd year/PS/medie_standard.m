% 1.a.

function [m1, m2] = medie_standard()
  x=[1 2 3 4];
  a=0.01;

  vm=mean(x);
  s=5;
  n=length(x);
  z=norminv(1-a/2,0,1);

  m1=vm-(s/sqrt(n))*z;
  m2=vm+(s/sqrt(n))*z;
  
  if nargout < 1
     m1 = [m1; m2];
  end
endfunction