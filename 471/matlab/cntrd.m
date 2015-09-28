n = [100, 500, 1000, 4000];
h = zeros(size(n));
err = zeros(size(n));

for i = 1:length(n)
  x = linspace(-1, 1, n(i)+1);
  h(i) = x(2)-x(1);
  y = sin(pi*x);
  dy = (y(3:end) - y(1:end-2))/(2*h(i));
  dyex = pi*cos(pi*x);
  e(i) = max(abs(dy-dyex(2:end-1)));
end
loglog(h, e);