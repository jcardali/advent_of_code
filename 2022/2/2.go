package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	f, _ := os.Open("input.txt")

	defer f.Close()

	scanner := bufio.NewScanner(f)
	totalScore := 0
	scoreMap := map[string]int{"A": 1, "B": 2, "C": 3}
	resultMap := map[string]int{"X": 0, "Y": 3, "Z": 6}

	for scanner.Scan() {
		var roundScore int
		round := scanner.Text()

		// A = Rock
		// B = Paper
		// C = Scissors
		// X = Lose
		// Y = Draw
		// Z = Win
		switch round {
		case "A X":
			roundScore = scoreMap["C"] + resultMap["X"]
		case "A Y":
			roundScore = scoreMap["A"] + resultMap["Y"]
		case "A Z":
			roundScore = scoreMap["B"] + resultMap["Z"]
		case "B X":
			roundScore = scoreMap["A"] + resultMap["X"]
		case "B Y":
			roundScore = scoreMap["B"] + resultMap["Y"]
		case "B Z":
			roundScore = scoreMap["C"] + resultMap["Z"]
		case "C X":
			roundScore = scoreMap["B"] + resultMap["X"]
		case "C Y":
			roundScore = scoreMap["C"] + resultMap["Y"]
		case "C Z":
			roundScore = scoreMap["A"] + resultMap["Z"]
		}

		totalScore += roundScore
	}
	fmt.Printf("Total score is: %d", totalScore)
}
