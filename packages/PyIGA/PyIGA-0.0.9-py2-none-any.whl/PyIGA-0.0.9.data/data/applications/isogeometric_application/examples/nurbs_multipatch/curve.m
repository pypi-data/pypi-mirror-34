knots = [ 0 0 0 0 0.4 0.4 0.4 0.4 1 1 1 1];
coefs = zeros(4,8);
coefs(:,1) = [ 0 0 0 1];
coefs(:,2) = [ 0.4 0 0 1];
coefs(:,3) = [ 0.64 0.16 0 1];
coefs(:,4) = [ 0.848 0.352 0 1];
coefs(:,5) = [ 0.848 0.352 0 1];
coefs(:,6) = [ 1.16 0.64 0 1];
coefs(:,7) = [ 1.4 1 0 1];
coefs(:,8) = [ 2 1 0 1];
patch1 = nrbmak(coefs,knots);
patch1_number = [ 1 2 3 4 5 6 7 8];

