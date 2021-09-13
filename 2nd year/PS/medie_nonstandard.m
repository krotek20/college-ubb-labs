% 1.b.

function [m1 m2] = medie_nonstandard()
  x=[1 2 3 4];
  a=0.01;
  
  vm=mean(x);
  sn=std(x);
  n=length(x);
  t=tinv(1-a/2,n-1);
  
  m1=vm-(sn/sqrt(n))*t;
  m2=vm+(sn/sqrt(n))*t;
  
  if nargout < 1
     m1 = [m1; m2];
  end
endfunction
