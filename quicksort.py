def quicksort(arr):
    def swap(arr, index1, index2):
        temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;

    def partition(arr, start, end):
        p_index = start;
        p_value = arr[start];
        swap(arr, p_index, end - 1);
        curr_index = start;
        for i in range(start, end - 1):
            if arr[i] < p_value:
                swap(arr, i, curr_index);
                curr_index += 1;
        swap(arr, curr_index, end - 1);
        return curr_index;

    def quicksort(arr, start, end):
        if start < end:
            pivot = partition(arr, start, end);
            quicksort(arr, start, pivot - 1);
            quicksort(arr, pivot, end - 1);

    quicksort(arr, 0, len(arr));