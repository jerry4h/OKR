# [127] 单词接龙
#

# @lc code=start
NOT_VISITED = 0
VISITED = 1
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if beginWord == endWord:
            return 1
        n = len(wordList)
        ref_dic = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                ref_dic[word[:i]+'*'+word[i+1:]].append(word)
        status = {w:NOT_VISITED for w in wordList}
        q = collections.deque([(1, beginWord)])
        
        # 单向查询，重复查找，效率较低，但能过。
        while q:
            step, word = q.popleft()
            status[word] = VISITED
            for i in range(len(word)):
                pattern = word[:i]+'*'+word[i+1:]
                for word_next in ref_dic[pattern]:
                    if word_next == endWord:
                        return step+1
                    if status[word_next] == NOT_VISITED:
                        q.append((step+1, word_next))
        return 0
