class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordlist = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in "abcdefghijklmnopqrstuvwxyz":
                            newword = w[:i] + c + w[i + 1:]
                            if newword in wordlist:
                                newlayer[newword] += [j + [newword] for j in layer[w]]
            wordlist -= set(newlayer.keys())
            layer = newlayer

        return res

# https://blog.csdn.net/chelseajcole/article/details/94089190