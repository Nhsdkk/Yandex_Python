from functools import lru_cache
import typing

MAX_ITEMS_LEN = 2
MAX_TREE_WIDTH = 3


class Node:
    # _is_root = True
    nodes = []
    items = []

    def __init__(self, is_root: bool = True, items: typing.Optional[list[int]] = None, l_node: typing.Self = None,
                 r_node: typing.Self = None) -> None:
        self._is_root = is_root
        self.items = items if items is not None else []
        if l_node is not None:
            self.nodes.append(l_node)
        if r_node is not None:
            self.nodes.append(r_node)

    def insert(self, value: int) -> typing.Optional[tuple[int, list[typing.Self]]]:
        if len(self.items) == 0:
            self.items.append(value)
            self.items.sort()
            return None

        if value > max(self.items) and len(self.nodes) != 0:
            result = self.nodes[-1].insert(value)

            if result is not None:
                self.nodes = self.nodes[:-1]
                self.items.append(result[0])
                self.nodes.extend(result[1])
                self.items.sort()
                self.nodes.sort()
                if self._is_root and len(self.nodes) > MAX_TREE_WIDTH and len(self.items) > MAX_ITEMS_LEN:
                    l_node1, r_node1 = self.nodes[0], self.nodes[1]
                    l_node2, r_node2 = self.nodes[-2], self.nodes[-1]
                    self.nodes = []
                    new_nodes = [
                        Node(is_root=False, items=[self.items[0]], l_node=l_node1, r_node=r_node1),
                        Node(is_root=False, items=[self.items[-1]], l_node=l_node2, r_node=r_node2)
                    ]
                    self.nodes = new_nodes
                    self.items = [self.items[1]]    
                    return None

                if len(self.nodes) > MAX_TREE_WIDTH and len(self.items) > MAX_ITEMS_LEN:
                    return (
                        self.items[1],
                        [
                            Node(is_root=False, items=[self.items[0]], l_node=self.nodes[0], r_node=self.nodes[1]),
                            Node(is_root=False, items=[self.items[-1]], l_node=self.nodes[-2], r_node=self.nodes[-1])
                        ]
                    )

            return None

        if value < min(self.items) and len(self.nodes) != 0:
            result = self.nodes[0].insert(value)

            if result is not None:
                self.nodes = self.nodes[1:]
                self.items.append(result[0])
                self.nodes.extend(result[1])
                self.items.sort()
                self.nodes.sort()
                if self._is_root and len(self.nodes) > MAX_TREE_WIDTH and len(self.items) > MAX_ITEMS_LEN:
                    l_node1, r_node1 = self.nodes[0], self.nodes[1]
                    l_node2, r_node2 = self.nodes[-2], self.nodes[-1]
                    self.nodes = []
                    new_nodes = [
                        Node(is_root=False, items=[self.items[0]], l_node=l_node1, r_node=r_node1),
                        Node(is_root=False, items=[self.items[-1]], l_node=l_node2, r_node=r_node2)
                    ]
                    self.nodes = new_nodes
                    self.items = [self.items[1]]
                    return None

                if len(self.nodes) > MAX_TREE_WIDTH and len(self.items) > MAX_ITEMS_LEN:
                    return (
                        self.items[1],
                        [
                            Node(is_root=False, items=[self.items[0]], l_node=self.nodes[0], r_node=self.nodes[1]),
                            Node(is_root=False, items=[self.items[-1]], l_node=self.nodes[-2], r_node=self.nodes[-1])
                        ]
                    )

                return None

        if len(self.items) < MAX_ITEMS_LEN:
            self.items.append(value)
            self.items.sort()
            return None

        if self._is_root:
            self.items.append(value)
            self.items.sort()
            self.nodes = [
                Node(is_root=False, items=[self.items[0]]),
                Node(is_root=False, items=[self.items[-1]])
            ]
            self.items = [self.items[1]]
            return None

        self.items.append(value)
        self.items.sort()

        return self.items[1], [Node(is_root=False, items=[self.items[0]]), Node(is_root=False, items=[self.items[-1]])]

    # debugging function
    def insert_r_node(self, node: typing.Self):
        self.nodes.append(node)

    # debugging function
    def insert_l_node(self, node: typing.Self):
        self.nodes.insert(0, node)

    # debugging function
    def insert_m_node(self, node: typing.Self):
        self.nodes.insert(1, node)

    def __contains__(self, item):
        if item in self.items:
            return True

        if item > max(self.items):
            if len(self.nodes) != 2:
                return False
            return item in self.nodes[-1]

        if item < min(self.items):
            if len(self.nodes) != 2:
                return False
            return item in self.nodes[0]

        if len(self.nodes) != 3:
            return False
        return item in self.nodes[1]

    def __repr__(self) -> str:
        info = dict()
        info["items"] = self.items
        if len(self.nodes) >= 3:
            info["m_node"] = repr(self.nodes[1])
        else:
            info["m_node"] = None

        if len(self.nodes) >= 2:
            info["r_node"] = repr(self.nodes[-1])
        else:
            info["r_node"] = None

        if len(self.nodes) >= 1:
            info["l_node"] = repr(self.nodes[0])
        else:
            info["l_node"] = None

        return str(info)

    def __lt__(self, other: typing.Self):
        return sum(self.items) < sum(other.items)
