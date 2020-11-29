package main

import "fmt"

// ListNode is a node in a singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	node1 := l1
	node2 := l2
	carry := 0
	sumNodes := make([]*ListNode, 0)
	for i := 0; node1 != nil || node2 != nil || carry == 1; i++ {
		num := 0

		if node1 != nil {
			num += node1.Val
			node1 = node1.Next
		}

		if node2 != nil {
			num += node2.Val
			node2 = node2.Next
		}

		if carry == 1 {
			num++
			carry = 0
		}

		if num > 9 {
			carry = 1
			num -= 10
		}

		node := ListNode{Val: num, Next: nil}
		sumNodes = append(sumNodes, &node)
		fmt.Println(num)

		if i > 0 {
			sumNodes[i-1].Next = &node
		}
	}

	return sumNodes[0]
}
