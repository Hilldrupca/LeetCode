package average

import "testing"

func TestAverageOfLevels(t *testing.T) {
    // Tree:
    //      3
    //     / \
    //    9   20
    //       /  \
    //      15   7
    root := &TreeNode {
        3,
        &TreeNode {
            9,
            nil,
            nil,
        },
        &TreeNode {
            20,
            &TreeNode {
                15,
                nil,
                nil,
            },
            &TreeNode {
                7,
                nil,
                nil,
            },
        },
    }
    
    want := []float64{3.0, 14.5, 11.0}
    got := AverageOfLevels(root)
    
    if len(want) == len(got) {
        for i, _ := range got {
            if got[i] != want[i] {
                t.Errorf("Got: %v, wanted: %v", got, want)
            }
        }
    } else {
        t.Errorf("Got: %v, wanted: %v", got, want)
    }
    
}

func TestEmptyTree (t *testing.T) {
    want := []float64{}
    got := AverageOfLevels(nil)
    
    if len(want) != len(got) {
        t.Errorf("Got: %v, wanted: %v", got, want)
    }
}
