a = 10; % Lower bound
b = 16; % Upper bound
mean_Xi = (a + b) / 2;
var_Xi = (b - a)^2 / 12;

n_values = [1, 2, 3, 10, 30, 100];
mean_Z = zeros(size(n_values));
var_Z = zeros(size(n_values));

for i = 1:length(n_values)
    n = n_values(i);
    mean_Z(i) = mean_Xi;
    var_Z(i) = var_Xi / n;
end

% Display the calculated mean and variance for each n
disp('n    mean_Z    var_Z');
disp([n_values, mean_Z, var_Z]);