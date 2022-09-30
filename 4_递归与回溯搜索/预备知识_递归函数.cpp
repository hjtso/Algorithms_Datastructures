#include <stdio.h>

int compute_sum(int i){
	if (i > 3){
		return 0;
	}
	return i + compute_sum(i+1);
}

int main(){
	printf("%d\n", compute_sum(1));
	return 0;
}

