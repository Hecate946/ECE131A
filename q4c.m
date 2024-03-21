t = 10000; % 10^4
a = 10; % Lower bound
b = 16; % Upper bound
X = a + (b-a) .* rand(100,t);

n_values = [1, 2, 3, 10, 30, 100];
mean_Xi = (a + b) / 2;
var_Xi = (b - a)^2 / 12;

mean_Z = zeros(size(n_values));
var_Z = zeros(size(n_values));

for i = 1:length(n_values)
    n = n_values(i);
    mean_Z(i) = mean_Xi;
    var_Z(i) = var_Xi / n;
end

figure
for j = 1:length(n_values)
    n = n_values(j);
    Z = zeros(1,t);
    for i = 1:n
        Z = Z + ((X(i,1:t))/n);
    end
    [h,c] = hist(Z, linspace(min(Z), max(Z), 100+1));
    
    z_sigma = sqrt(var_Z(j));
    x = min(Z):(1 / (n + 1)):max(Z);
    y = (1/(z_sigma*sqrt(2*pi))) * exp(-(x-mean_Z(j)).^2/(2*z_sigma^2));
    
    subplot(3,2,j)
    bar(c,h/trapz(c,h))
    hold on
    plot(x, y,'r')
    hold off
    xlabel('x')
    ylabel('f_X (x)')
    legend({'PDF of Z_n', 'Gaussian Overlay'},'Location','northwest')
    title(['PDF of Z_n (n = ', num2str(n), ')'])
end
