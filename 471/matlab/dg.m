function zz = dg(z)
  x = z(1);
  y = z(2);
  zz = zeros(2, 2);
  zz(1, 1) = 2 + 200*(6*x^2 - 2*y);
  zz(1, 2) = -400*x;
  zz(2, 1) = -400*x;
  zz(2, 2) = 200;