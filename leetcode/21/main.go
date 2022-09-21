package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	listNode1 := list1
	listNode2 := list2
	var firstNode *ListNode // points at the first node of the result list
	var currentNode *ListNode

	for {
		if listNode1 == nil && listNode2 == nil {
			break
		}

		if listNode1 != nil && listNode2 != nil {
			if listNode1.Val < listNode2.Val {
				if firstNode == nil {
					firstNode = listNode1
					currentNode = firstNode
				} else {
					currentNode.Next = listNode1
					currentNode = currentNode.Next
				}
				listNode1 = listNode1.Next
			} else {
				if firstNode == nil {
					firstNode = listNode2
					currentNode = firstNode
				} else {
					currentNode.Next = listNode2
					currentNode = currentNode.Next
				}
				listNode2 = listNode2.Next
			}
		} else if listNode1 != nil {
			if firstNode == nil {
				firstNode = listNode1
				currentNode = firstNode
			} else {
				currentNode.Next = listNode1
				currentNode = currentNode.Next
			}
			listNode1 = listNode1.Next
		} else if listNode2 != nil {
			if firstNode == nil {
				firstNode = listNode2
				currentNode = firstNode
			} else {
				currentNode.Next = listNode2
				currentNode = currentNode.Next
			}
			listNode2 = listNode2.Next
		}
	}

	return firstNode
}

func main() {
	list1 := ListNode{
		Val: 1, Next: &ListNode{
			Val: 2, Next: &ListNode{
				Val:  4,
				Next: nil,
			},
		},
	}

	list2 := ListNode{
		Val: 1, Next: &ListNode{
			Val: 3,
			Next: &ListNode{
				Val:  4,
				Next: nil,
			},
		},
	}

	newList := mergeTwoLists(&list1, &list2)

	i := 0
	for newList != nil {
		fmt.Printf("%d: %d\n", i, newList.Val)
		newList = newList.Next
		i++
	}
}
