function [route]= kadai2()
% 初期値
p = [0,0,0,0,0];
d = [0,inf,inf,inf,inf];
s = [0,0,0,0,0];
startKey = 1;
final = size(p,2);

% 距離が0の時でも適用できるようにつながりがない要素を-1とする
graph = [-1,50,80,-1,-1;-1,-1,20,15,-1;-1,-1,-1,10,15;-1,-1,-1,-1,30;-1,-1,-1,-1,-1];

% ダイクストラ法
[s, d, p]= Duijkstras(s, d, p, graph, startKey);

% 求めるrouteが反転したものを求める
routeR = [final];
i = 2;
key = final;
while p(1,key) != 0
	key = p(1,key);
	routeR(1,i) = key;
	i = i+1;
end

% 最短routeを求める
i = size(routeR,2);
route =[];
while (i>0)
    route(1,size(routeR,2)-i+1) = routeR(1,i);
    i = i -1;
end
