function [optimizedValue, optimizedSolutions] = solutionOfKnapsackProblem(c,a,b)
    %function [optimizedValue, optimizedSolutions] = solutionOfKnapsackProblem(c,a,b)
    % c: Coefficient vector of the objective function
    % a: Coefficient vector of the constraint
    % b: Value of the constraint
    %
    % 適用できる形にソート
    [sortedC,sortedA,beforeKey] = sortForKnapsack(c,a,b);
    % 貪欲法で初期暫定解を求める。
    [iniResults, iniMax] = greedy(sortedC,sortedA,b);

    partValues = [-1];

    % 分枝限定法
    [optimizedValue, optimizedSolutions] = branchAndBound(sortedC,sortedA,b,iniMax,iniResults,partValues);

    % ソートして最適解を求めたので、元に戻す。
    optimizedSolutions = sortWithBeforeKey(optimizedSolutions,beforeKey);
endfunction
