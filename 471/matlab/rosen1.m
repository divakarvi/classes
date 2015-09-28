x = [2.2; 2.7];
for i = 1:10
  x = newt(x, @g, @dg);
  i
  err = norm(x - [1;1])
end