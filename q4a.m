t = 10000; % 10^4
a = 10; % Lower bound
b = 16; % Upper bound
X = a + (b-a) .* rand(100,t);

figure
for n = [1, 2, 3, 10, 30, 100]
    Z = zeros(1,t);
    for i = 1:n
        Z = Z + ((X(i,1:t))/n);
    end
    [h,c] = hist(Z, linspace(min(Z), max(Z), 100+1));
    
    subplot(3,2,find([1, 2, 3, 10, 30, 100] == n))
    bar(c,h/trapz(c,h))
    xlabel('x')
    ylabel('f_X (x)')
    legend({'PDF of Z_n'},'Location','northwest')
    title(['PDF of Z_n (n = ', num2str(n), ')'])
    grid on
end
