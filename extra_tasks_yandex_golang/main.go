package main

import (
	"extra_tasks_yandex_golang/b_tree"
	"fmt"
)

func createBTree() *b_tree.Node {
	node1 := b_tree.Node{}
<<<<<<< HEAD
	node2 := b_tree.Node{}
	node3 := b_tree.Node{}
	node4 := b_tree.Node{}

	node2.Create([]int{5, 6}, []*b_tree.Node{}, false)
	node3.Create([]int{3}, []*b_tree.Node{}, false)
	node4.Create([]int{1}, []*b_tree.Node{}, false)
	node1.Create([]int{2, 4}, []*b_tree.Node{&node4, &node3, &node2}, true)
	//node1.Create([]int{}, []*b_tree.Node{}, true)
=======
	//node2 := b_tree.Node{}
	//node3 := b_tree.Node{}
	//node4 := b_tree.Node{}

	//node2.Create([]int{5, 6}, []*b_tree.Node{}, false)
	//node3.Create([]int{3}, []*b_tree.Node{}, false)
	//node4.Create([]int{1}, []*b_tree.Node{}, false)
	//node1.Create([]int{2, 4}, []*b_tree.Node{&node4, &node3, &node2}, true)
	node1.Create([]int{}, []*b_tree.Node{}, true)
>>>>>>> b_tree

	return &node1
}

func testBTree(tree *b_tree.Node) {
	fmt.Println(tree.Repr())
<<<<<<< HEAD
	arr := []int{7, 6, 6}
	for _, i := range arr {
		if i == 6 {
			tree.Insert(6)
			fmt.Println(tree.Repr())
=======
	for i := 1; i < 8; i++ {
		if i == 5 {
			tree.Insert(5)
>>>>>>> b_tree
			continue
		}
		tree.Insert(i)
		fmt.Println(tree.Repr())
<<<<<<< HEAD
		fmt.Println(i)
=======
>>>>>>> b_tree
	}

}

func main() {
	btreePtr := createBTree()
	testBTree(btreePtr)
}
