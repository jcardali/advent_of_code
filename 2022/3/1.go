package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func main() {
	f, _ := os.Open("input.txt")

	defer f.Close()

	scanner := bufio.NewScanner(f)
	var totalPriority int32 = 0

	for scanner.Scan() {
		rucksack := scanner.Text()
		rucksackLength := len(rucksack)
		compartment1 := rucksack[:rucksackLength/2]
		compartment2 := rucksack[rucksackLength/2:]

		charMap := map[string]bool{}
		for _, charInt := range compartment1 {
			charMap[string(charInt)] = true
		}

		for _, charInt := range compartment2 {
			char := string(charInt)
			if charMap[char] {
				if unicode.IsUpper(charInt) {
					totalPriority += charInt - int32(38)
				} else {
					totalPriority += charInt - int32(96)
				}
				break
			}
		}
	}
	fmt.Printf("Total priority is: %d", totalPriority)
}
