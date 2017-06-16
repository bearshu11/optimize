function notSortedSolutions = sortWithBeforeKey(sortedSolutions,beforeKey)
    for i=1:size(sortedSolutions,2)
    	notSortedSolutions(1,i) = -1;
    end
    for i=1:size(sortedSolutions,2)
    	notSortedSolutions(1,beforeKey(1,i)) = sortedSolutions(1,i);
    end
endfunction
