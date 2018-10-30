from collections import Counter

times = int(input())

for i in range(0,times):

    word1 = input()
    word2 = input()

    word1len = Counter(word1)
    word2len = Counter(word2)

    common = word1len & word2len
    common_al = list(common.elements())

    commonCharLen = len(common_al)

    ans1 = len(word1) - commonCharLen
    ans2 = len(word2) - commonCharLen

    if len(common_al) == 0:
        ans = len(word1) + len(word2)

    elif len(word1) == commonCharLen:
        ans = ans2
    elif len(word2)== ans2:
        ans = ans1
else:
    ans = ans1+ans2


print(ans)