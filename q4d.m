t = 10000;
X = create_die_rv([100 t]);

mu = 6.235;
var = 11.595;

for n = [1 2 3 10 30 100]
    M = zeros(1, t);
    for i = 1:n
        M = M + ((X(i, 1:t)) / n);
    end
    [h, c] = hist(M, (min(M):(1 / (n + 1)):max(M)));
    
    figure
    subplot(2, 1, 1)
    stem(c, h / trapz(c, h))
    xlabel('x')
    ylabel('fX (x)')
    legend({'PDF of Z_n'}, 'Location', 'northwest')
    title(['PDF OF Z' num2str(n) ' For Unfair Die (n = ' num2str(n) ')'])
    grid on

    z_sigma = sqrt(var/n);
    x = min(M):(1 / (n + 1)):max(M);
    y = (1/(z_sigma*sqrt(2*pi))) * exp(-(x-mu).^2/(2*z_sigma^2));
    
    subplot(2,1,2)
    stem(c,h/trapz(c,h))
    hold on
    plot(x,y,'r')
    hold off
    xlabel('x')
    ylabel('fX (x)')
    legend({'Gaussian Distribution - G_n', 'PDF of Z_n'},'Location','northwest')
    title(['Superimposed PDF Zn and Gn For Unfair Die(n = ' num2str(n) ')'])
    grid on
end
