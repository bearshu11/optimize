function [optimizedValue, optimizedSolutions] = solutionOfKnapsackProblem(c,a,b)
     [c,a] = sortForKnapsack(c,a,b);
     [iniResults, iniMax] = greedy(c,a,b);
     partValues = [-1];
     [optimizedValue, optimizedSolutions] = branchAndBound(c,a,b,iniMax,iniResults,partValues);
endfunction
