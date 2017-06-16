function [iniResults, iniMax] = greedy(c,a,b)
	% [c,a] = sortForKnapsack(c,a,b);
	iniResults = [];
	iniMax = 0;
	for i=1:size(c,2)
		b = b - a(1,i);
		if b >= 0
			iniResults(1,i) = 1;
			iniMax = a(1,i);
		else
			b = b + a(1,i);
			iniResults(1,i) = 0;
		endif
	end
endfunction
