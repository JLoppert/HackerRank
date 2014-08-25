class Node:
    left = None;
    right = None;
    data = None;

    def __init__(self, data):
        self.data = data;

    def __str__(self):
        return str(self.data);

    def find(self, data):
        if data == self.data:
            return self;
        elif data < self.data and self.left:
            self.left.find(data);
        elif data > self.data and self.right:
            self.right.find(data);
        else:
            print(str(data) + ' not found');

    # def find_parent(self, data):
    #     if data == self.data:
    #         return self;
    #     elif data < self.data and self.left:
    #         self.left.find(data);
    #     elif data > self.data and self.right:
    #         self.right.find(data);
    #     else:
    #         print(str(data) + ' not found');

    def insert(self, data):
        if data < self.data:
            if self.left:
                self.left.insert(data);
            else:
                self.left = Node(data);
        elif self.right:
            self.right.insert(data);
        else:
            self.right = Node(data);

    def delete(self, data):
        return;

    def max(self):
        if self.right:
            return self.right.max();
        else:
            return self;

    def min(self):
        if self.left:
            return self.left.min();
        else:
            return self;

    def depth(self):
        if not self:
            return 0;

        left = 0;
        right = 0;
        if self.left:
            left = self.left.depth();

        if self.right:
            right = self.right.depth();

        return 1 + max(left, right);

    def pre_order(self):
        if self:
            print(self.data, end = ' ');

        if self.left:
            self.left.pre_order();

        if self.right:
            self.right.pre_order();

    def in_order(self):
        if self.left:
            self.left.in_order();

        if self:
            print(self.data, end = ' ');

        if self.right:
            self.right.in_order();

    def post_order(self):
        if self.left:
            self.left.post_order();

        if self.right:
            self.right.post_order();

        if self:
            print(self.data, end = ' ');


tree = Node(10);
tree.insert(5);
tree.insert(15);
tree.insert(3);
tree.insert(12);
tree.insert(17);
tree.insert(7);
tree.insert(13);
tree.in_order();
print();
tree.pre_order();
print()
tree.post_order();
print();
print(tree.depth());
print(tree.max());
print(tree.min());