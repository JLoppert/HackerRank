N, T = input().split(' ');
widths = [int(i) for i in input().split(' ')];
for i in range(int(T)):
    start, end = input().split(' ');
    start = int(start);
    end = int(end);
    print(min(widths[start:end+1]));