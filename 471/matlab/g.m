function zz = g(z)
  x = z(1);
  y = z(2);
  zz = zeros(2, 1);
  zz(1) = 2*(x-1) + 200*(x*x - y)*(2*x);
  zz(2) = 200*(y - x*x);
