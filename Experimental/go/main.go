package main

import (
	"fmt"
	"golang.org/x/exp/constraints"
)

func GeneratePascal[T constraints.Integer](numRows int) [][]T {
	if numRows <= 0 {
		return nil
	}

	triangle := make([][]T, numRows)

	for i := 0; i < numRows; i++ {
		rowSize := i + 1
		triangle[i] = make([]T, rowSize)
		triangle[i][0] = 1
		triangle[i][rowSize-1] = 1

		for j := 1; j < i; j++ {
			triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
		}
	}

	return triangle
}

func main() {
	triangle := GeneratePascal[int](5)
	for _, row := range triangle {
		for _, val := range row {
			fmt.Printf("%d ", val)
		}
		fmt.Println()
	}
}
