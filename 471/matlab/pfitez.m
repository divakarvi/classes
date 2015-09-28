t = [1804, 1927, 1960, 1974, 1987, 1999]';
p = [1, 2, 3, 4, 5, 6]';
d = 3
P = polyfit(t, p, d);

tt = [1804:1999]';
pp = polyval(P, tt);
plot(t, p, 'o', 'MarkerFaceColor', 'k');
hold on
plot(tt, pp)

tt = [2000:2050]';
pp = polyval(P, tt);
plot(tt, pp, 'LineWidth', 3);