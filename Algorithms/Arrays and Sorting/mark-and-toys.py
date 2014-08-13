N, K = [int(i) for i in input().split(' ')];
prices = [int(i) for i in input().split(' ')];
prices.sort();
index = 0
while K > 0 and K > prices[index]:
    K -= prices[index];
    index += 1;

print(index);