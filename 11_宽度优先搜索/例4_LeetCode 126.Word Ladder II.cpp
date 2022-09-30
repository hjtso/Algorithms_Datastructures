#include <stdio.h>

#include <vector>
#include <string>
#include <map>

bool connect(std::string &word1, std::string &word2){
	int cnt = 0;
	for (int i = 0; i < word1.length(); i++){
		if (word1[i] != word2[i]){
			cnt++;
		}
	}
	return cnt == 1;
}

void construct_graph(std::string &beginWord,
			std::vector<std::string>& wordList,
 	 		std::map<std::string, std::vector<std::string> > &graph){
	int has_begin_word = 0;
	for (int i = 0; i < wordList.size(); i++){
		if (wordList[i] == beginWord){
 			has_begin_word = 1;
  		}
		graph[wordList[i]] = std::vector<std::string>();
	}
 	for (int i = 0; i < wordList.size(); i++){
 		for (int j = i + 1; j < wordList.size(); j++){
  			if (connect(wordList[i], wordList[j])){
   				graph[wordList[i]].push_back(wordList[j]);
     			graph[wordList[j]].push_back(wordList[i]);
       		}
       	}
       	if (has_begin_word == 0 && connect(beginWord, wordList[i])){
	       	graph[beginWord].push_back(wordList[i]);
		}
   	}
}

struct Qitem{
	std::string node;
	int parent_pos;
	int step;
	Qitem(std::string _node, int _parent_pos, int _step)
		: node(_node), parent_pos(_parent_pos), step(_step){
	}
};

void BFS_graph(std::string &beginWord, std::string &endWord,
			std::map<std::string, std::vector<std::string> > &graph,
			std::vector<Qitem> &Q,
			std::vector<int> &end_word_pos){
	std::map<std::string, int> visit;
	int min_step = 0;
 	Q.push_back(Qitem(beginWord.c_str(), -1, 1));
 	visit[beginWord] = 1;
	int front = 0;
	while(front != Q.size()){
		const std::string &node = Q[front].node;
		int step = Q[front].step;
		if (min_step != 0 && step > min_step){
			break;
		}
		if (node == endWord){
			min_step = step;
			end_word_pos.push_back(front);
		}
		const std::vector<std::string> &neighbors = graph[node];
		for (int i = 0; i < neighbors.size(); i++){
			if (visit.find(neighbors[i]) == visit.end() ||
				visit[neighbors[i]] == step + 1){
				Q.push_back(Qitem(neighbors[i], front, step + 1));
				visit[neighbors[i]] = step + 1;
			}
		}
 		front++;
	}
}

class Solution {
public:
    std::vector<std::vector<std::string> > findLadders(
		std::string beginWord, std::string endWord,
		std::vector<std::string>& wordList) {
		std::map<std::string, std::vector<std::string> > graph;
		construct_graph(beginWord, wordList, graph);
		std::vector<Qitem> Q;
        std::vector<int> end_word_pos;
		BFS_graph(beginWord, endWord, graph, Q, end_word_pos);
        std::vector<std::vector<std::string> > result;
        for (int i = 0; i < end_word_pos.size(); i++){
        	int pos = end_word_pos[i];
        	std::vector<std::string> path;
        	while(pos != -1){
        		path.push_back(Q[pos].node);
				pos = Q[pos].parent_pos;
        	}
        	result.push_back(std::vector<std::string>());
        	for (int j = path.size() - 1; j >= 0; j--){
	        	result[i].push_back(path[j]);
	        }
        }
        return result;
    }
};

int main(){	
	std::string beginWord = "hit";
	std::string endWord = "cog";
	std::vector<std::string> wordList;
	wordList.push_back("hot");
	wordList.push_back("dot");
	wordList.push_back("dog");
	wordList.push_back("lot");
	wordList.push_back("log");
	wordList.push_back("cog");
	Solution solve;
	std::vector<std::vector<std::string> > result 
		= solve.findLadders(beginWord, endWord, wordList);	
	for (int i = 0; i < result.size(); i++){
		for (int j = 0; j < result[i].size(); j++){
			printf("[%s] ", result[i][j].c_str());
		}
		printf("\n");
	}
	return 0;
}
