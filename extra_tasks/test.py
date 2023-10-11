from b_tree.b_tree import Node


def test_b_tree():
    b_tree = Node()
    print(b_tree.__repr__())
    b_tree.insert(1)
    print(b_tree.__repr__())
    b_tree.insert(2)
    print(b_tree.__repr__())
    b_tree.insert(3)
    print(b_tree.__repr__())
    b_tree.insert(4)
    print(b_tree.__repr__())
    b_tree.insert(5)
    print(b_tree.__repr__())


if __name__ == "__main__":
    test_b_tree()
