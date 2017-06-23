function [s, d, p]= Duijkstras(s, d, p, graph, startKey)
% s:接点の配列(0:探索前,1:探索済み)
% d:startKeyからの最短距離の配列
% p:最短路における直前の接点の配列(初期値0)
% graph:問題のネットワーク
% startKey:初期位置

% 調べる場所を1に変更する
s(1,startKey) = 1;

% _s_:探索前の接点の集合が空集合であるかどうかの判定
condition = false;
for i=1:size(s,2)
	if s(1,i) == 0
		condition = true;
		break;
	endif
end

% _s_が空集合でないとき
if condition == true
	for arrival=1:size(s,2)
		% _s_に属するもののみ大小判定する
		if s(1,arrival) == 0
			dValue = graph(startKey,arrival);
			if dValue != -1
				% より小さい最短経路が見つかれば変更する
				if d(1,arrival) > dValue + d(1,startKey)
					d(1,arrival) = dValue + d(1,startKey);
					p(1,arrival) = startKey;
				endif
			endif
		endif
	end

	% 最小のものを見つけて次のstartKeyにする
	min = inf;
	nextKey = 0;
	for arrival=1:size(s,2)
		if s(1,arrival) == 0
			if min > d(1,arrival)
				min = d(1,arrival);
				nextKey = arrival;
			endif
		endif
	end

	[s,d,p] = Duijkstras(s,d,p,graph,nextKey);
endif
