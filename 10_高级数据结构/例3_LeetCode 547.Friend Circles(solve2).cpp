#include <stdio.h>

#include <vector>

class DisjointSet{
public:
	DisjointSet(int n){
		for (int i = 0; i < n; i++){
			_id.push_back(i);
			_size.push_back(1);
		}
		_count = n;
	}
	int find(int p){
		while(p != _id[p]){
			_id[p] = _id[_id[p]];
			p = _id[p];
		}
		return p;
	}
	void union_(int p, int q){
		int i = find(p);
		int j = find(q);
		if (i == j){
			return;
		}
		if (_size[i] < _size[j]){
			_id[i] = j;
			_size[j] += _size[i];
		}
		else{
			_id[j] = i;
			_size[i] += _size[j];
		}
		_count--;
	}
	int count(){
		return _count;
	}
private:
	std::vector<int> _id;
	std::vector<int> _size;
	int _count;
};

class Solution {
public:
    int findCircleNum(std::vector<std::vector<int> >& M) {
    	DisjointSet disjoint_set(M.size());
    	for (int i = 0; i < M.size(); i++){
	    	for (int j = i + 1; j < M.size(); j++){
	    		if (M[i][j]){
		    		disjoint_set.union_(i, j);
		    	}
	    	}
	    }
    	return disjoint_set.count();
    }
};

int main(){
	int test[][3] = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
	std::vector<std::vector<int> > M(3, std::vector<int>(3, 0));
	for (int i = 0; i < 3; i++){
		for (int j = 0; j < 3; j++){
			M[i][j] = test[i][j];
		}
	}
	Solution solve;
	printf("%d\n", solve.findCircleNum(M));
	return 0;
}
