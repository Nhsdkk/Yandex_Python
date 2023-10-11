from typing import Optional

MAX_ITEMS_LEN = 2
MAX_TREE_WIDTH = 3


class Node:
    __is_root = True
    __l_node = None
    __m_node = None
    __r_node = None
    items = []

    def __init__(self, is_root: bool = True, items: Optional[list[int]] = None) -> None:
        self.__is_root = is_root
        self.items = items if items is not None else []
        pass

    def __split(self, upper_level_tree_width: int) -> Optional[int]:
        if self.__is_root and self.__r_node is not None and self.__l_node is not None and self.__m_node is not None:
            l_value = self.items.pop(0)
            r_value = self.items.pop()

            self.__l_node = Node(is_root=False, items=[l_value])
            self.__m_node = Node(is_root=False, items=[r_value])

            return None
        else:
            if upper_level_tree_width != MAX_TREE_WIDTH:
                l_value = self.items.pop(0)
                mid_value = self.items.pop(0)
                # not final here

    def insert(self, value: int) -> None:
        if self.__r_node is None and self.__l_node is None:
            self.items.append(value)
            self.items.sort()
        else:
            max_v = self.items[1] if len(self.items) == MAX_ITEMS_LEN else self.items[0]
            min_v = self.items[0]
            if value < min_v:
                self.__l_node.insert(value)
            elif min_v < value < max_v:
                self.__m_node.insert(value)
            elif max_v < value and self.__r_node is not None:
                self.__r_node.insert(value)
            else:
                self.__m_node.insert(value)

        if len(self.items) > MAX_ITEMS_LEN:
            upper_level_tree_width = sum([1 for node in [self.__l_node, self.__m_node, self.__r_node] if node is not None])
            split_result = self.__split(upper_level_tree_width=upper_level_tree_width)
            # not final here

    def __repr__(self) -> dict:
        info = dict()
        info["items"] = self.items
        info["l_node"] = self.__l_node.__repr__() if self.__l_node is not None else None
        info["m_node"] = self.__m_node.__repr__() if self.__m_node is not None else None
        info["r_node"] = self.__r_node.__repr__() if self.__r_node is not None else None
        return info
