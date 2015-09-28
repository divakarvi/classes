t = [2013, 2010, 2005, 2000, 1995, 1990, 1980]';
g = [9184, 5931, 2257, 1198, 728, 390, 303]';

d = 2
P = polyfit(t, g, d);

tt = [1980:2013]';
gg = polyval(P, tt);

plot(t, g, 'o', 'MarkerFaceColor', 'k');
hold on;
plot(tt, gg);

tt = [2013:2033]';
gg = polyval(P, tt);
plot(tt, gg, 'LineWidth', 3);