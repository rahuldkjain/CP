import sys
t = int(sys.stdin.readline())
for _ in range(t):
    pSum = 0
    nSum = 0
    count = 0
    result = 0
    N = int(input())
    nArr = []
    A = list(map(int,sys.stdin.readline().strip().split()))

    for ele in A:
        if (ele >= 0):
            count = count + 1
            pSum = pSum + ele
        else:
            nSum = nSum + ele
            nArr.append(ele)

    if(pSum == 0):
        print(nSum)
    else:
        nArr.sort(reverse=True)
        result = pSum*count
        for ele in nArr:
            pSum += ele
            nSum -= ele
            count += 1
            temp = (pSum*count)+nSum
            result = max(result,temp)
        print(result)

