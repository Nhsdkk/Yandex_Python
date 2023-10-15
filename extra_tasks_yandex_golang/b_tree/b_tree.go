package b_tree

import (
	"extra_tasks_yandex_golang/b_tree/utils"
	"fmt"
	"slices"
	"sort"
)

const MaxItemAmount = 2
const MaxChildrenAmount = 3

type Node struct {
	children []*Node
	values   []int
	isRoot   bool
}

func (n *Node) Create(values []int, children []*Node, isRoot bool) {
	n.children = children
	n.values = values
	n.isRoot = isRoot
}

func (n *Node) modifyChildren(index int, children []*Node) {
	n.children = append(n.children[:index], n.children[index+1:]...)
	n.children = append(n.children, children...)
	sort.Slice(n.children, func(i, j int) bool {
		return utils.Sum(n.children[i].values) < utils.Sum(n.children[j].values)
	})
}

func (n *Node) modifyValues(value int) {
	n.values = append(n.values, value)
	sort.Ints(n.values)
}

func (n *Node) splitNode() (value int, nodes []*Node) {
	var children1, children2 []*Node
	if len(n.children) != 0 && len(n.children)%2 == 1 {
		children1, children2 = n.children[:len(n.values)/2], n.children[len(n.values)/2:]
	} else if len(n.children) != 0 && len(n.children)%2 == 0 {
		children1, children2 = n.children[:len(n.values)/2+1], n.children[len(n.values)/2+1:]
	}
	node1, node2 := &Node{isRoot: false, values: n.values[:len(n.values)/2], children: children1}, &Node{isRoot: false, values: n.values[len(n.values)/2+1:], children: children2}
	return n.values[len(n.values)/2], []*Node{node1, node2}
}

func (n *Node) splitRootNode() {
	value, nodes := n.splitNode()
	n.children = nodes
	n.values = []int{value}
}

func (n *Node) Insert(value int) (valueToAdd int, nodesToAdd []*Node, isEmpty bool) {
	if len(n.values) == 0 {
		n.values = append(n.values, value)
		sort.Ints(n.values)
		return 0, nil, true
	}

	if value > slices.Max(n.values) && len(n.children) >= 2 {
		fmt.Println(fmt.Sprintf("Inserting to end in node %s...", n.Repr()))
		valueResult, nodesResult, emptyResult := n.children[len(n.children)-1].Insert(value)
		if emptyResult {
			return 0, nil, true
		}
		n.modifyChildren(len(n.children)-1, nodesResult)
		n.modifyValues(valueResult)

		if len(n.values) > MaxItemAmount && len(n.children) > MaxChildrenAmount {
			if n.isRoot {
				n.splitRootNode()
				return 0, nil, true
			}

			splitValue, splitNodes := n.splitNode()

			return splitValue, splitNodes, false
		}
		return 0, nil, true
	}

	if len(n.children) != 0 {
		for i, compareValue := range n.values {
			if value <= compareValue {
				fmt.Println(fmt.Sprintf("Inserting to index %v node %s...", i, n.Repr()))
				valueResult, nodesResult, emptyResult := n.children[i].Insert(value)
				if emptyResult {
					return 0, nil, true
				}
				n.modifyChildren(i, nodesResult)
				n.modifyValues(valueResult)

				if len(n.values) > MaxItemAmount && len(n.children) > MaxChildrenAmount {
					if n.isRoot {
						n.splitRootNode()
						return 0, nil, true
					}

					splitValue, splitNodes := n.splitNode()

					return splitValue, splitNodes, false
				}
				return 0, nil, true
			}
		}
	}

	if len(n.values) < MaxItemAmount {
		n.modifyValues(value)
		return 0, nil, true
	}

	if n.isRoot {
		n.modifyValues(value)
		n.splitRootNode()
		return 0, nil, true
	}

	n.modifyValues(value)
	splittedValue, splittedNodes := n.splitNode()

	return splittedValue, splittedNodes, false
}

func (n *Node) Includes(value int) bool {
	if slices.Contains(n.values, value) {
		return true
	}

	if len(n.values) == 0 {
		return false
	}

	if slices.Max(n.values) < value {
		if len(n.children) < 2 {
			return false
		}
		return n.children[len(n.children)-1].Includes(value)
	}

	if slices.Min(n.values) > value {
		if len(n.children) == 0 {
			return false
		}
		return n.children[0].Includes(value)
	}

	for i := 1; i < len(n.values); i-- {
		if value < n.values[i] {
			return n.children[i].Includes(value)
		}
	}

	return false
}

func (n *Node) Remove(value int) (valueToAdd int, nodesToAdd []*Node, isEmpty bool) {
	//TODO implement me
	panic("implement me")
}

func (n *Node) Repr() string {
	itemString := ""

	if len(n.values) == 0 {
		itemString = "Nil"
	} else {
		for _, item := range n.values {
			itemString += fmt.Sprintf("%v, ", item)
		}
		itemString = itemString[:len(itemString)-2]
	}

	childrenString := ""

	if len(n.children) == 0 {
		childrenString = "Nil"
	} else {
		for _, child := range n.children {
			childrenString += fmt.Sprintf("%s, ", child.Repr())
		}
		childrenString = childrenString[:len(childrenString)-2]
	}

	return fmt.Sprintf("{Values: [%s], Children: [%s]}", itemString, childrenString)
}
