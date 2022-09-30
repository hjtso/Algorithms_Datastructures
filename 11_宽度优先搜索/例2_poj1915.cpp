#include <stdio.h>
#include <queue>

#define MAXN 310

struct location{
	int x;
	int y;
	int cnt;
	location (int _x, int _y, int _cnt) :
		x(_x), y(_y), cnt(_cnt){
	}
};

static const int dx[] = {-2, -1, 1, 2, 2, 1, -1, -2};
static const int dy[] = {-1, -2, -2, -1, 1, 2, 2, 1};

int BFS_move(int beginx, int beginy, int endx, int endy, int n){
	int mark[MAXN][MAXN] = {0};
	std::queue<location> Q;
	location loc(beginx, beginy, 0);
	Q.push(loc);
	mark[beginx][beginy] = 1;
	while(!Q.empty()){
		loc = Q.front();
		Q.pop();
		if (loc.x == endx && loc.y == endy){
			return loc.cnt;
		}
		for (int i = 0; i < 8; i++){
			int newx = dx[i] + loc.x;
			int newy = dy[i] + loc.y;
			if (newx < 0 || newy < 0 ||
				newx >= n || newy >= n || mark[newx][newy]){
				continue;
			}
			Q.push(location(newx, newy, loc.cnt + 1));
			mark[newx][newy] = 1;
		}
	}
	return -1;
}

int main(){
	int t;
	int n;
	int beginx;
	int beginy;
	int endx;
	int endy;
	scanf("%d", &t);
	while(t--){
		scanf("%d %d %d %d %d", &n, &beginx, &beginy, &endx, &endy);
		printf("%d\n", BFS_move(beginx, beginy, endx, endy, n));
	}
	return 0;
}

//https://blog.csdn.net/Jaihk662/article/details/78634106
//https://blog.csdn.net/u013480600/article/details/25502441?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.control