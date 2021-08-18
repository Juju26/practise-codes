'''
127.word ladder (https://leetcode.com/problems/word-ladder/)

'''

from collections import deque
def ladderLength(s1,s2,s3) -> int:
    s3=set(s3)
    if s2 not in s3:
        return 0
    else:
        alp="abcdefghijklmnopqrstuvwxyz"
        qu=deque([(s1,1)])
        vis=set([s1])
        while qu:
            pr,ne=qu.popleft()
            for i in range(len(pr)):
                for j in alp:
                    s=pr[:i]+j+pr[i+1:]
                    if s in s3:
                        if s==s2:
                            return ne+1
                        elif s not in vis:
                            vis.add(s)
                            qu.append((s,ne+1))
    return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
p=ladderLength(beginWord,endWord,wordList)
print(p)

"""

better run time 

from collections import deque
class Solution:
    def ladderLength(self, s1: str, s2: str, s3: List[str]) -> int:
        if s2 not in s3:
            return 0
        nei=collections.defaultdict(list)
        s3.append(s1)
        
        for word in s3:
            for j in range(len(word)):
                pattern=word[:j]+"*"+word[j+1:]
                nei[pattern].append(word)
        visit=set([s1])
        q=deque([s1])
        res=1
        while q:
            for i in range(len(q)):
                word=q.popleft()
                if word==s2:
                    return res
                for j in range(len(word)):
                    pattern=word[:j]+"*"+word[j+1:]
                    for ne in nei[pattern]:
                        if ne not in visit:
                            visit.add(ne)
                            q.append(ne)
            res+=1
        return 0

"""