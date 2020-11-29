/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func rangeSumBST(root *TreeNode, low int, high int) int {
    sum := 0
    
    if root == nil {
        return sum
    }
    
    fmt.Println(root.Val)
    
    if root.Val >= low {
        sum += rangeSumBST(root.Left, low, high)
    }

    if root.Val <= high {
        sum += rangeSumBST(root.Right, low, high)
    }
    
    if root.Val >= low && root.Val <= high {
        sum += root.Val
    }    
    
    return sum
}

