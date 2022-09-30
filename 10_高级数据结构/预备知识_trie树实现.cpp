#include <stdio.h>

#include <string>
#include <vector>

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

class TrieTree{
public:
	TrieTree(){
	}
	~TrieTree(){
		for (int i = 0; i < _node_vec.size(); i++){
			delete _node_vec[i];
		}
	}
	void insert(const char *word) {
		TrieNode *ptr = &_root;
        while(*word){
        	int pos = *word - 'a';
        	if (!ptr->child[pos]){
	        	ptr->child[pos] = new_node();
	        }
	        ptr = ptr->child[pos];
        	word++;
        }
        ptr->is_end = true;
    }    
    bool search(const char *word){
    	TrieNode *ptr = &_root;
        while(*word){
        	int pos = *word - 'a';
        	if (!ptr->child[pos]){
	        	return false;
	        }
	        ptr = ptr->child[pos];
        	word++;
        }
        return ptr->is_end;
    }
    bool startsWith(const char *prefix){
    	TrieNode *ptr = &_root;
        while(*prefix){
        	int pos = *prefix - 'a';
        	if (!ptr->child[pos]){
	        	return false;
	        }
	        ptr = ptr->child[pos];
        	prefix++;
        }
        return true;
    }
    TrieNode *root(){
    	return &_root;
    }
private:
	TrieNode *new_node(){
		TrieNode *node = new TrieNode();
		_node_vec.push_back(node);
		return node;
	}
	std::vector<TrieNode *> _node_vec;
	TrieNode _root;
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

void get_all_word_from_trie(TrieNode *node, std::string &word,
				   std::vector<std::string> &word_list){
	for (int i = 0; i < TRIE_MAX_CHAR_NUM; i++){
		if (node->child[i]){
			word.push_back(i + 'a');
			if (node->child[i]->is_end){
				word_list.push_back(word);
			}
			get_all_word_from_trie(node->child[i], word, word_list);
			word.erase(word.length()-1, 1);
		}
	}
}

int main(){
	TrieTree trie_tree;
	trie_tree.insert("abcd");
	trie_tree.insert("abc");
	trie_tree.insert("abd");
	trie_tree.insert("b");
	trie_tree.insert("bcd");
	trie_tree.insert("efg");
	printf("preorder_trie:\n");
	preorder_trie(trie_tree.root(), 0);
	printf("\n");	
	std::vector<std::string> word_list;
	std::string word;
	printf("All words:\n");
	get_all_word_from_trie(trie_tree.root(), word, word_list);
	for (int i = 0; i < word_list.size(); i++){
		printf("%s\n", word_list[i].c_str());
	}
	printf("\n");
	printf("Search:\n");
	printf("abc : %d\n", trie_tree.search("abc"));
	printf("abcd : %d\n", trie_tree.search("abcd"));
	printf("bc : %d\n", trie_tree.search("bc"));
	printf("b : %d\n", trie_tree.search("b"));
	printf("\n");
	printf("ab : %d\n", trie_tree.startsWith("ab"));
	printf("abc : %d\n", trie_tree.startsWith("abc"));
	printf("bc : %d\n", trie_tree.startsWith("bc"));
	printf("fg : %d\n", trie_tree.startsWith("fg"));
	return 0;
}
