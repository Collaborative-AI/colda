from collections import Counter


def getPalindromesCount(s):
    count = Counter([''])
    res = 0
    mod = 10 ** 9 + 7
    for c in s:
        for i, d in list(count.items()):
            i += c
            if len(i) < 5: 
                count[i] += d
                print('this is d',d)
                print('this is count[i]',count)
            elif (i == i[::-1])&(len(i)==5):
                res += d
            
    return res % mod

result = getPalindromesCount("010110")



print(result)