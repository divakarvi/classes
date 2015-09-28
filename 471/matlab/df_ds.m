function zz = df_ds(z)
  x1 = z(1);
  x2 = z(2);
  zz = zeros(2, 2);
  zz(1, 1) = 2*x1;
  zz(1, 2) = 2*x2;
  zz(2, 1) = exp(x1-1);
  zz(2, 2) = 3*x2^2;