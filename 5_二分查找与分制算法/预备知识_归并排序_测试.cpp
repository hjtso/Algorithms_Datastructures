
#include <vector>

void merge_sort_two_vec(std::vector<int> &sub_vec1,
						std::vector<int> &sub_vec2,
						std::vector<int> &vec){
	int i = 0;
	int j = 0;
	while(i < sub_vec1.size() && j < sub_vec2.size()){
		if (sub_vec1[i] <= sub_vec2[j]){
			vec.push_back(sub_vec1[i]);
			i++;
		}
		else{
			vec.push_back(sub_vec2[j]);
			j++;
		}
	}
	for (; i < sub_vec1.size(); i++){
		vec.push_back(sub_vec1[i]);
	}
	for (; j < sub_vec2.size(); j++){
		vec.push_back(sub_vec2[j]);
	}
}

void merge_sort(std::vector<int> &vec){
	if (vec.size() < 2){
		return;
	}
	int mid = vec.size() / 2;
	std::vector<int> sub_vec1;
	std::vector<int> sub_vec2;
	for (int i = 0; i < mid; i++){
		sub_vec1.push_back(vec[i]);
	}
	for (int i = mid; i < vec.size(); i++){
		sub_vec2.push_back(vec[i]);
	}
	merge_sort(sub_vec1);
	merge_sort(sub_vec2);
	vec.clear();
	merge_sort_two_vec(sub_vec1, sub_vec2, vec);
}

#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <assert.h>
int main(){
	std::vector<int> vec1;
	std::vector<int> vec2;
	srand(time(NULL));
	for (int i = 0; i < 10000; i++){
		int num = (rand() * rand()) % 100003;
		vec1.push_back(num);
		vec2.push_back(num);
	}
	merge_sort(vec1);
	std::sort(vec2.begin(), vec2.end());
	assert(vec1.size() == vec2.size());
	for (int i = 0; i < vec1.size(); i++){
		assert(vec1[i] == vec2[i]);
	}
	return 0;
}
