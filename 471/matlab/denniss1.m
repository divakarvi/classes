x = [2.0; 0.5];
for i = 1:10
  x = newt(x, @f_ds, @df_ds);
  norm(x-[1;1])
end