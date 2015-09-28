function xx = newt(x, f, df)
  xx = x - feval(df, x)\feval(f,x);