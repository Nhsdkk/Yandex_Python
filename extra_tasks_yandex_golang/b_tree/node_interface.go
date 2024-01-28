package b_tree

type NodeInterface interface {
	Create(values []int, children []*Node, isRoot bool)
	Insert(value int) (valueToAdd int, nodesToAdd []*Node, isEmpty bool)
	Includes(value int) bool
	Remove(value int) (valueToAdd int, nodesToAdd []*Node, isEmpty bool)
	Repr() string
}
