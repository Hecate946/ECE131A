function matrix = create_die_rv(nx)
    size = 1:12;
    dist = [1/17 2/17 2/17 1/17 2/17 1/17 2/17 1/17 1/17 1/17 2/17 1/17];
    cdist = cumsum(dist); % Cumulative distribution
    matrix = zeros(nx(1),nx(2));
    for column = 1:nx(1)
        for row = 1:nx(2)
            r = rand; % Random number between 0 and 1
            matrix(column,row) = size(find(r <= cdist, 1));
        end
    end
end
