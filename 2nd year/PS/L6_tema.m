pkg load statistics;

n = 1000;
nr = 0;
total = 0;
i2_counter = 0;
v = zeros(1, n);

for i = 1 : n
  i2 = 0;
  if rand() > 0.4
    v(i) = unifrnd(4, 6);
    i2 = 1;
  else
    v(i) = exprnd(1/5);
  endif
  if v(i) > 5
    total++;
    nr = nr + 1;
    if i2 == 1
      i2_counter++;
    endif
  endif
endfor

% a.
vm = mean(v)
ds = std(v)
% b.
pb = nr / n
% c.
pi2 = i2_counter / total
