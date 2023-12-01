package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func isVisible(x int, y int, trees [][]int) bool {
	height := trees[y][x]
	fmt.Println(x, y)
	for i := 0; i <= x; i++ {
		if i == x {
			return true
		}
		if trees[y][i] < height {
			continue
		} else {
			break
		}
	}
	for i := 0; i <= y; i++ {
		if i == y {
			return true
		}
		if trees[i][y] < height {
			continue
		} else {
			break
		}
	}
	//for i := x; i <= 4; i++ {
	//	if i == 4 {
	//		return true
	//	}
	//	if trees[y][i] < height {
	//		continue
	//	} else {
	//		break
	//	}
	//}
	return false
}

func main() {
	f, _ := os.Open("input.txt")

	defer f.Close()

	scanner := bufio.NewScanner(f)
	var trees [][]int

	for scanner.Scan() {
		line := scanner.Text()
		var row []int

		for _, tree := range line {
			height, _ := strconv.Atoi(string(tree))
			row = append(row, height)
		}
		trees = append(trees, row)
	}

	numVisibleTrees := 0

	for y, row := range trees {
		for x, _ := range row {
			if y == 0 || y == len(trees)-1 || x == 0 || x == len(row)-1 {
				numVisibleTrees += 1
			} else {
				// fmt.Println(x, y)
				if isVisible(x, y, trees) {
					numVisibleTrees += 1
				}
			}
		}
	}
	fmt.Println(numVisibleTrees)
}
