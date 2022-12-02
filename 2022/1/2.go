package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	f, _ := os.Open("input.txt")

	defer f.Close()

	scanner := bufio.NewScanner(f)
	calorieCounts := []int{}
	currCalories := 0

	for scanner.Scan() {
		calories, err := strconv.Atoi(scanner.Text())

		// Empty line
		if err != nil {
			calorieCounts = append(calorieCounts, currCalories)
			currCalories = 0
		} else {
			currCalories += calories
		}
	}

	sort.Ints(calorieCounts)

	calorieCountsLen := len(calorieCounts)
	topThree := calorieCounts[calorieCountsLen-3 : calorieCountsLen]
	topThreeCalories := 0

	for _, calories := range topThree {
		topThreeCalories += calories
	}

	fmt.Printf("Sum of top three calories is: %d", topThreeCalories)
}
