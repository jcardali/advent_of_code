package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, _ := os.Open("input.txt")

	defer f.Close()

	scanner := bufio.NewScanner(f)
	containedPairs := 0
	overlappingPairs := 0

	for scanner.Scan() {
		pairsStr := scanner.Text()
		pairs := strings.Split(pairsStr, ",")
		assignment1 := strings.Split(pairs[0], "-")
		assignment2 := strings.Split(pairs[1], "-")
		assignment1Start, _ := strconv.Atoi(assignment1[0])
		assignment1End, _ := strconv.Atoi(assignment1[1])
		assignment2Start, _ := strconv.Atoi(assignment2[0])
		assignment2End, _ := strconv.Atoi(assignment2[1])

		if assignment1Start <= assignment2Start && assignment1End >= assignment2End ||
			assignment1Start >= assignment2Start && assignment1End <= assignment2End {
			containedPairs += 1
		}

		if assignment1Start <= assignment2End && assignment2End <= assignment1End ||
			assignment2Start <= assignment1End && assignment1End <= assignment2End {
			overlappingPairs += 1
		}
	}
	fmt.Printf("Number of contained pairs is: %d\n", containedPairs)
	fmt.Printf("Number of overlapping pairs is: %d", overlappingPairs)
}
