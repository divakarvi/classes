t = [1804, 1927, 1960, 1974, 1987, 1999]';
p = [1, 2, 3, 4, 5, 6]';
p = 1e9*p;
lp = log(p);

d = 2
A = zeros(length(t), d+1);

for i = 1:d+1
  A(:,i) = t.^(i-1);
end

c = A\lp;

tt = [1804:1999]';
AA = zeros(length(tt), d+1);
for i = 1:d+1
  AA(:,i) = tt.^(i-1);
end
lpp = AA*c;
pp = exp(lpp);

plot(t, p, 'o', 'MarkerFaceColor', 'k');
hold on
plot(tt, pp) 

tt = [2000:2050]';
AA = zeros(length(tt), d+1);
for i = 1:d+1
  AA(:,i) = tt.^(i-1);
end
lpp = AA*c;
pp = exp(lpp);
plot(tt, pp, 'LineWidth', 3)