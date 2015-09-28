function yy = lgrng(x, y, xx)
%x = grid points
%y = function values at grid points
%xx = points at which interp is evaluated
%yy = interpolated values
  
 w = lgrnweights(x);
 yy = zeros(size(xx));

 for i = 1:length(xx)
   dx = xx(i)-x;
   yy(i) = prod(dx)*sum((y.*w)./dx);
 end

 function w = lgrnweights(x)
 w = zeros(size(x));
 for i = 1:length(x)
   dx = x(i)-x;
   dx(i) = 1.0;
   w(i) = 1/prod(dx);
 end
