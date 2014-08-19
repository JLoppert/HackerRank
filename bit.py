# binary indexed tree
class Node:
    def __init__(self, value):
        self.left = None;
        self.right = None;
        self.value = value;

class BIT:
    def __init__(self, array):
        frequency_array = self.to_frequency_array(array);

    def to_frequency_array(old, op = lambda x,y: x - y):
        new = [old[0]];
        for i in range(1, len(old)):
            new.append(op(old[i], old[i-1]));

        return new;

# def to_binary_index(index):
#     while index != 0 and index & 1 == 0:
#         index = index >> 1;

#     index = index >> 1;
#     return index;

# def cumulative_sum(index, array):
#     index = to_binary_index(index);
#     while index != 0:

# # Write out node n in binary.
# # Set the counter to 0.
# # Repeat the following while n ≠ 0:
# # Add in the value at node n.
# # Remove the leftmost 1 bit from n.


a = [5, 6, 21, 32, 84, 112, 112];
b = to_frequency_array(a);
print(a, b);