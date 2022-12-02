package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	f, _ := os.Open("input.txt")

	defer f.Close()

	scanner := bufio.NewScanner(f)
	maxCalories := 0
	currCalories := 0

	for scanner.Scan() {
		calories, err := strconv.Atoi(scanner.Text())

		// Empty line
		if err != nil {
			if currCalories > maxCalories {
				maxCalories = currCalories
			}
			currCalories = 0
		} else {
			currCalories += calories
		}
	}

	fmt.Printf("Maximum calories is: %d", maxCalories)
}
