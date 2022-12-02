package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	f, _ := os.Open("input.txt")

	defer f.Close()

	scanner := bufio.NewScanner(f)
	totalScore := 0
	scoreMap := map[string]int{"X": 1, "Y": 2, "Z": 3}

	for scanner.Scan() {
		var resultScore int
		round := scanner.Text()

		// A, X = Rock
		// B, Y = Paper
		// C, Z = Scissors
		if round == "A Y" || round == "B Z" || round == "C X" {
			resultScore = 6
		} else if round == "A X" || round == "B Y" || round == "C Z" {
			resultScore = 3
		} else if round == "A Z" || round == "B X" || round == "C Y" {
			resultScore = 0
		}

		shapes := strings.Split(round, " ")
		shape2 := shapes[1]

		shapeScore := scoreMap[shape2]

		totalScore += shapeScore + resultScore
	}
	fmt.Printf("Total score is: %d", totalScore)
}
