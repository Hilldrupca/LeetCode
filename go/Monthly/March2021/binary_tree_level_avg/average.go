// LeetCode Monthly Challenge problem for March 5th, 2021.
package average

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}

// AverageOfLevels returns the average node value for each level of a binary tree.
// An empty slice is returned if the tree is empty.
func AverageOfLevels(root *TreeNode) []float64 {
    var res []float64
    
    if root == nil { return res }
    
    var stack []TreeNode
    stack = append(stack, *root)
    
    for len(stack) > 0 {
        n := len(stack)
        sum := 0
        
        for i := 0; i < n; i++ {
            node := stack[0]
            stack = stack[1:]
            
            sum += node.Val
            
            if node.Left != nil {
                stack = append(stack, *node.Left)
            }
            
            if node.Right != nil {
                stack = append(stack, *node.Right)
            }
        }
        
        res = append(res, float64(sum) / float64(n))
    }
    
    return res
}
