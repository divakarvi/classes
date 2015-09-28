n = 100;
assert(mod(n, 4) == 0);

A = randn(n, n/4);
A = [A, A + 1e-6*randn(n, n/4)];
xe = randn(n/2, 1);
b = A*xe;

x1 = (A'*A)\(A'*b);

[Q, R] = qr(A, 0);
x2 = R\(Q'*b);

x3 = A\b;

cond_num = cond(A)
err_normal = norm(x1 - xe)/norm(xe)
err_qr = norm(x2 - xe)/norm(xe)
err_matlab = norm(x3 - xe)/norm(xe)


