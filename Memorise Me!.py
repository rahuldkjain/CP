
N = int(input())
A = [int(x) for x in input().split()]
count = [0]*1000000
for ele in A:
    count[ele] += 1
Q = int(input())
for i in range(Q):
    temp = int(input())
    if(count[temp] == 0):
        print('NOT PRESENT')
    else:
        print(count[temp])

#for best time complexity
"""
from sys import stdin, stdout
from collections import Counter     
input()                                                     //N
cnt = Counter(stdin.readline().rstrip().split())            //counting after each input
input()                                                      //Q
quers = stdin.read().splitlines()                            
rez = [str(cnt.get(i,'NOT PRESENT')) for i in quers]
stdout.write('\n'.join(rez))


"""