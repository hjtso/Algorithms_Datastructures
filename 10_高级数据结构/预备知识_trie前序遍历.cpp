#include <stdio.h>

#define TRIE_MAX_CHAR_NUM 26

struct TrieNode{
	TrieNode *child[TRIE_MAX_CHAR_NUM];
	bool is_end;
	TrieNode() : is_end(false){
		for (int i = 0; i < TRIE_MAX_CHAR_NUM; i++){
			child[i] = 0;
		}
	}
};

void preorder_trie(TrieNode *node, int layer){
	for (int i = 0; i < TRIE_MAX_CHAR_NUM; i++){
		if (node->child[i]){
			for (int j = 0; j < layer; j++){
				printf("---");
			}
			printf("%c", i + 'a');
			if (node->child[i]->is_end){
				printf("(end)");
			}
			printf("\n");
			preorder_trie(node->child[i], layer + 1);
		}
	}
}

int main(){
	TrieNode root;
	TrieNode n1;
	TrieNode n2;
	TrieNode n3;
	root.child['a'-'a'] = &n1;
	root.child['b'-'a'] = &n2;
	root.child['e'-'a'] = &n3;
	n2.is_end = true;
	
	TrieNode n4;
	TrieNode n5;
	TrieNode n6;
	n1.child['b'-'a'] = &n4;
	n2.child['c'-'a'] = &n5;
	n3.child['f'-'a'] = &n6;
		
	TrieNode n7;
	TrieNode n8;
	TrieNode n9;
	TrieNode n10;
	n4.child['c'-'a'] = &n7;
	n4.child['d'-'a'] = &n8;
	n5.child['d'-'a'] = &n9;
	n6.child['g'-'a'] = &n10;
	n7.is_end = true;
	n8.is_end = true;
	n9.is_end = true;
	n10.is_end = true; 
	
	TrieNode n11;
	n7.child['d'-'a'] = &n11;
	n11.is_end = true;
	
	preorder_trie(&root, 0);
	
	return 0;
}
