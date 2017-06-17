function [resultC,resultA,beforeKey] = sortForKnapsack(c,a,b)
    r =[];
    for i=1:size(c,2)
        r(1,i) = c(1,i) / a(1,i);
    end

    [after,beforeKey] = sort(r,"descend");

    resultA = [];
    resultC = [];
    for i=1:size(c,2)
        resultC(1,i) = c(1,beforeKey(1,i));
        resultA(1,i) = a(1,beforeKey(1,i));
    end
endfunction
