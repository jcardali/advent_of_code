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
	groupCharMap := map[string]int{}
	count := 0

	for scanner.Scan() {
		rucksack := scanner.Text()
		charMap := map[string]bool{}

		for _, charInt := range rucksack {
			char := string(charInt)
			if v, ok := groupCharMap[char]; ok {
				if !charMap[char] {
					if v+1 == 3 {
						if unicode.IsUpper(charInt) {
							totalPriority += charInt - int32(38)
						} else {
							totalPriority += charInt - int32(96)
						}
						break
					} else {
						groupCharMap[char] = v + 1
					}
				}
			} else {
				groupCharMap[char] = 1
			}

			charMap[char] = true
		}

		count++

		// Reset
		if count > 2 {
			count = 0
			groupCharMap = map[string]int{}
		}
	}
	fmt.Printf("Total priority is: %d", totalPriority)
}
