import sys

def compliment(a):
    if(a == 1):
        return 0
    elif(a == 0):
        return 1
#N[0] = N, N[1] = Q
N = list(map(int,sys.stdin.readline().strip().split()))

A = list(map(int,sys.stdin.readline().strip().split()))

for _ in range(N[1]):
    B = list(map(int,sys.stdin.readline().strip().split()))

    if(B[0] == 1):
        A[B[1] - 1] = compliment(A[B[1]-1])

    else:
        if(A[B[2]-1] == 1):
            print('ODD')
        else:
            print('EVEN')

