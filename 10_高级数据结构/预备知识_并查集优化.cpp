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
	void print_set(){
		printf("ÔªËØ: ");
		for (int i = 0; i < _id.size(); i++){
			printf("%d ", i);
		}
		printf("\n");
		printf("¼¯ºÏ: ");
		for (int i = 0; i < _id.size(); i++){
			printf("%d ", _id[i]);
		}
		printf("\n");
	}
	int count(){
		return _count;
	}
private:
	std::vector<int> _id;
	std::vector<int> _size;
	int _count;
};

int main(){
	DisjointSet disjoint_set(8);
	disjoint_set.print_set();
	printf("Union(0, 5)\n");
	disjoint_set.union_(0, 5);
	disjoint_set.print_set();
	printf("Find(0) = %d, Find(5) = %d\n",
						disjoint_set.find(0), disjoint_set.find(5));
	printf("Find(2) = %d, Find(5) = %d\n",
						disjoint_set.find(2), disjoint_set.find(5));
	disjoint_set.union_(2, 4);
	disjoint_set.print_set();
	disjoint_set.union_(0, 4);
	disjoint_set.print_set();
	printf("Find(2) = %d, Find(5) = %d\n",
						disjoint_set.find(2), disjoint_set.find(5));
	return 0;
}
