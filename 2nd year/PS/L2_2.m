N = 500;
contor = 0;

rectangle('Position', [0 0 1 1], 'FaceColor', 'w')
axis square
hold on

for i = 1:N

  x = rand;
  y = rand;
  M = [x,y]; CE = [0.5, 0.5];
  A = [1,0]; B=[0,1]; C=[0,0]; D=[1,1];
  vect = [pdist([M;A]) pdist([M;B]) pdist([M;C]) pdist([M;D])];
  minim = min(vect);
  if pdist([M;CE]) < minim
    contor++;
    plot(x,y,'b','MarkerSize',10)
  endif
endfor

contor/N