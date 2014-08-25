def subset(arr):
    new = [];
    ss = [];

    for index, value in enumerate(arr):
        ss.append(gen_subset(arr, new, [], index));

    print(ss);


def gen_subset(original, current, myList, index):
    current.append(original[index]);
    print(index, current);
    myList.append(current);

    for i in range(index+1, len(original)):
        print(index, current, myList, i);
        gen_subset(original, current, myList, i);

    current.pop(-1);
    return myList;


subset([1, 2, 3, 4]);