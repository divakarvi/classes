function zz = f_ds(z)
  x1 = z(1);
  x2 = z(2);
  zz = zeros(2, 1);
  zz(1) = x1^2 + x2^2 - 2;
  zz(2) = exp(x1-1) + x2^3 - 2;