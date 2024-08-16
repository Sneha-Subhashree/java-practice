def find_modified_bowl(N, marbles):
    for i in range(N-1, 0, -1):
        if marbles[i]<9:
            marbles[i] +=1
            if marbles[i]==9:
                j=i-1
                while j>=0 and marbles[j]==9:
                  marbles[j]=0
                  j-=1
                if j>=0:
                    marbles[j] +=1
            return i+1
        return 0
N=int(input())
marbles=list(map(int,input().split()))
print(find_modified_bowl(N,marbles))
                  