from b_tree.b_tree import Node
from sys import setrecursionlimit


def test_find_b_tree():
    b_tree = Node(items=[2, 4])
    b_tree.insert_l_node(Node(items=[1]))
    b_tree.insert_m_node(Node(items=[3]))
    b_tree.insert_r_node(Node(items=[5, 6]))
    print([i in b_tree for i in range(1, 8)])


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
    b_tree.insert(6)
    print(b_tree.__repr__())
    b_tree.insert(7)
    print(b_tree.__repr__())


if __name__ == "__main__":
    # setrecursionlimit(999999)
    test_b_tree()
    # test_find_b_tree()