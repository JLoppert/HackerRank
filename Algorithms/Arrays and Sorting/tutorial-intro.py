needle = int(input());
haystack_size = int(input());
haystack = [int(i) for i in input().split()];

index = int(haystack_size / 2)
window = index;
while window != 0:
    #print(needle, index, haystack[index], window);
    if haystack[index] == needle:
        #print('found');
        print(index);
        break;
    elif haystack[index] > needle:
        window = int((window+1)/2);
        index = index - window;
        #print('\tneedle < haystack, search left', needle, index, window);
    elif haystack[index] < needle:
        window = int((window+1)/2);
        index = index + window;
        #print('\tneedle > haystack, search right', needle, index, window);