function [resultR, resultC, resultA, x] = greedy2(c,a,b)

r =[];
for i=1:size(c,2)
	r(1,i) = c(1,i) / a(1,i);
end

[resultR,before] = sort(r,"descend");

resultA = [];
resultC = [];
for i=1:size(c,2)
	resultC(1,i) = c(1,before(1,i));
	resultA(1,i) = a(1,before(1,i));
end

x=[];
for i=1:size(c,2)
	b = b - resultA(1,i);
	if b >= 0
		x(1,i) = 1;
	else
		b = b + resultA(1,i); 
		x(1,i) = 0;
	endif
end

endfunction