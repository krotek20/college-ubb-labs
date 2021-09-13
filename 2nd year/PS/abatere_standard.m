% 1.c.

function [m1 m2] = abatere_standard(x)
  % x - vector
  a=0.01;
  
  n=length(x);
  sn=std(x);
  c1=chi2inv(1-a/2, n-1);
  c2=chi2inv(a/2, n-1);
  
  m1=sqrt((n-1)/c1)*sn;
  m2=sqrt((n-1)/c2)*sn;
  
  if nargout < 1
     m1 = [m1; m2];
  end
endfunction
