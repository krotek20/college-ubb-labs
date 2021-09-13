N = 500;

rectangle('Position', [0 0 1 1], 'FaceColor', 'w')
axis square
hold on

for i = 1:N

  obt = 0;
  asc = 0;
  x = rand();
  y = rand();
  M = [x,y];
  A = [1,0]; B=[0,1]; C=[0,0]; D=[1,1];
  LA = pdist([M;A]);
  LB = pdist([M;B]);
  LC = pdist([M;C]);
  LD = pdist([M;D]);
  
  if(LA^2 + LB^2 < 1)
    obt = obt + 1;
  endif
  if(LA^2 + LB^2 > 1)
    asc = asc + 1;
  endif
  if(LB^2 + LC^2 < 1)
    obt = obt + 1;
  endif
  if(LB^2 + LC^2 > 1)
    asc = asc + 1;
  endif
  if(LC^2 + LD^2 < 1)
    obt = obt + 1;
  endif
  if(LC^2 + LD^2 > 1)
    asc = asc + 1;
  endif
  if(LD^2 + LA^2 < 1)
    obt = obt + 1;
  endif
  if(LD^2 + LA^2 > 1)
    asc = asc + 1;
  endif
  
  if (obt == 2 && asc == 2)
    contor++;
    plot(x,y,'b','MarkerSize',10)
  endif
endfor

contor/N