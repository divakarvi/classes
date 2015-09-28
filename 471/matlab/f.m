function zz = f(z)
   x = z(1);
   y = z(2);
   zz = (1 - x)^2 + 100*(y-x*x)^2;
   