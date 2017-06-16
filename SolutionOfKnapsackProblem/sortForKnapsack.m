function [resultC,resultA] = sortForKnapsack(c,a,b)
    r =[];
    for i=1:size(c,2)
    	r(1,i) = c(1,i) / a(1,i);
    end

    [after,before] = sort(r,"descend");

    resultA = [];
    resultC = [];
    for i=1:size(c,2)
    	resultC(1,i) = c(1,before(1,i));
    	resultA(1,i) = a(1,before(1,i));
    end
endfunction
