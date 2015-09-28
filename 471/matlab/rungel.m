x = cheb(50);
xx = linspace(-1, 1, 200)*0.99;
y = 1.0./(1+10*x.^2);
yy = lgrng(x, y, xx);

plot(x, y, 'ro');
hold on
plot(xx, yy);
