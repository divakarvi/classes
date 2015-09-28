t = [2013, 2010, 2005, 2000, 1995, 1990, 1980]';
g = [9184, 5931, 2257, 1198, 728, 390, 303]';

d = 2

A = zeros(length(t), d+1);
for i = 1:d+1
  A(:, i) = t.^(i-1);
end
c = A\g;

tt = [1980:2013]';
AA = zeros(length(tt), d+1);
for i = 1:d+1
  AA(:, i) = tt.^(i-1);
end
gg = AA*c;

plot(t, g, 'o', 'MarkerFaceColor', 'k');
hold on;
plot(tt, gg);

tt = [2013:2033]';
AA = zeros(length(tt), d+1);
for i = 1:d+1
  AA(:, i) = tt.^(i-1);
end
gg = AA*c;

plot(tt, gg, 'LineWidth', 3);