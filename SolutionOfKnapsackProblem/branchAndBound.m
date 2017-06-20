function [iniMax, iniResults, partValues] = branchAndBound(c,a,b,iniMax,iniResults,partValues)
% [iniMax, iniResults, partValues] = branchAndBound(c,a,b,iniMax,iniResults,partValues)
% This program finds a solution of Knapsack problem by branch and bound method.
%    Objective function  max( ```math \sum_{i=1}^n c_i x_i ``` )
%    Constraint          ```math \sum_{i=1}^n a_i x_i \leq b ```
%                           x_i = 0,1 (i = 1...n)
%                           c_1/a_1 >= c_2/a_2 >= ... >= c_n/a_n
% c: Coefficient vector of the objective function(sorted)
% a: Coefficient vector of the constraint(sorted)
% b: Value of the constraint
% iniMax: Provisional value
% iniResult: Provisional solution
% partValues: set of partial problems
%             e.g. P(J0,J1), J0 = {1,2}, J1 = {3}, F = {4,5} => partValues == [0,0,1,-1,-1]
%
% Conditions
% size(a,2) == size(c,2) == size(iniResults)  partValues == (size(a,2) || [-1])

% ベクトルの長さは全て同じ
arraySize = size(c,2);

if partValues(1,1) == -1
    % P(J0,J1)でJ0={},J1={}の時
    for i=1:arraySize
        partValues(1,i) =  -1;
    end
    partValues(1,1) = 0;
    [iniMax,iniResults] = branchAndBound(c,a,b,iniMax,iniResults,partValues);
    partValues(1,1) = 1;
    [iniMax,iniResults] = branchAndBound(c,a,b,iniMax,iniResults,partValues);
else
    conditionToContinue = true;
    tempB = b;
    tempResults = [];
    tempMax = 0;
    % 連続緩和問題を解く処理
    for i=1:arraySize
        if partValues(1,i) == 0
            tempResults(1,i) = 0;
        elseif partValues(1,i) == 1
            tempResults(1,i) = 1;
            tempB -= a(1,i);
            if tempB <= 0
                if i < arraySize
                    for j=(i+1):arraySize
                        tempResults(1,j) = 0;
                    end
                endif
                if tempB < 0
                    conditionToContinue = false;
                    break;
                endif
                for j=1:arraySize
                    tempMax += c(1,j) * tempResults(1,j);
                end
                break;
            endif
        else
            tempB -= a(1,i);
            if tempB > 0
                tempResults(1,i) = 1;
            else
                if tempB == 0
                    tempResults(1,i) = 1;
                else
                    tempB += a(1,i);
                    tempResults(1,i) = tempB / a(1,i);
                    % tempB = 0;
                endif
                if i < arraySize
                    for j=(i+1):arraySize
                        tempResults(1,j) = 0;
                    end
                endif
                for j=1:arraySize
                    tempMax += c(1,j) * tempResults(1,j);
                end
                break;
            endif
        endif
    end

    % 実行可能解をもつかの判定  持たなければ終端
    if conditionToContinue == true
        % 0-1条件の確認
        condition01 = true;
        for i=1:arraySize
            if (tempResults(1,i) < 1 && tempResults(1,i) > 0)
                condition01 = false;
                break;
            endif
        end

        if condition01 == true
            if tempMax >= iniMax
                iniMax = tempMax;
                iniResults = tempResults;
                % 終端
            endif
        else
            % 暫定値よりも目的関数の値が大きいかどうか判定  大きくなければ終端
            if tempMax >= iniMax
                nextKey = -1;
                for i=1:arraySize
                    if (partValues(1,i) == -1)
                        nextKey = i;
                        break;
                    endif
                end
                if (nextKey != -1)
                    partValues(1,nextKey) = 0;
                    [iniMax,iniResults] = branchAndBound(c,a,b,iniMax,iniResults,partValues);
                    partValues(1,nextKey) = 1;
                    [iniMax,iniResults] = branchAndBound(c,a,b,iniMax,iniResults,partValues);
                else
                    iniMax = tempMax;
                    iniResults = tempResults;
                    % 木構造を最下層まで探索したので終端
                endif
            endif
        endif
    endif
endif
