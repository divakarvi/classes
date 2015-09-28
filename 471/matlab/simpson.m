n = [100, 500, 1000, 4000];
h = zeros(size(n));
err = zeros(size(n));

for i = 1:length(n)
  x = linspace(0, 1, n(i)+1);
  y = sin(pi*x);

  h(i) = x(2)-x(1);
  s = h(i)/3*(y(1) + y(end) + 4.0*sum(y(2:2:end-1)) + 2.0*sum(y(3:2:end-2)));
  err(i) = abs(s - 2.0/pi);
end

loglog(h, err)
	   