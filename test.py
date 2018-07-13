from sys import stdin, stdout
from collections import Counter
input()
cnt = Counter(stdin.readline().rstrip().split())
input()
quers = stdin.read().splitlines()
rez = [str(cnt.get(i,'NOT PRESENT')) for i in quers]
stdout.write('\n'.join(rez))