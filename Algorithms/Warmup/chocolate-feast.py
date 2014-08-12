T = int(input())

for i in range(T):

    N,C,M = str(input()).split()
    answer = 0
    # Compute Answer
    answer = int(int(N) / int(C));
    chocolates = answer;

    while chocolates >= int(M):
        chocolates -= int(M) - 1;
        answer += 1;

    print(answer);
