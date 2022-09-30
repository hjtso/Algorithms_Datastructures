
#include <stdio.h>
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

int main(){
	std::vector<int> vec;
	int test[] = {5, -7, 9, 8, 1, 4, -3, 10, 2, 0};
	for (int i = 0; i < 10; i++){
		vec.push_back(test[i]);
	}
	merge_sort(vec);
	for (int i = 0; i < vec.size(); i++){
		printf("[%d]", vec[i]);
	}
	printf("\n");
	return 0;
}
