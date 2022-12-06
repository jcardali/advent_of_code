package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Stack []string

type Stacks map[string]Stack

func parseInstruction(s string) (int, string, string) {
	split := strings.Split(s, " ")
	count, _ := strconv.Atoi(split[1])
	return count, split[3], split[5]
}

func executeInstruction(stacks Stacks, count int, from string, to string) {
	for i := 0; i < count; i++ {
		// fmt.Println(stacks)
		crate := stacks[from][0]
		stacks[from] = stacks[from][1:]
		// fmt.Println(crate)
		// fmt.Println(updatedFromStack)
		stacks[to] = append(Stack{crate}, stacks[to]...)
		// fmt.Println(stacks)
	}
}

func main() {
	f, _ := os.Open("input.txt")

	defer f.Close()

	scanner := bufio.NewScanner(f)
	var instructions []string
	var numStacks int
	var stacks = Stacks{}

	for scanner.Scan() {
		row := scanner.Text()
		instructions = append(instructions, row)
		if row == "" {
			numberRow := instructions[len(instructions)-2]
			numStacks, _ = strconv.Atoi(string(numberRow[len(numberRow)-2]))
			// fmt.Println(numStacks)
			for i := 0; i < numStacks; i++ {
				stacks[strconv.Itoa(i+1)] = Stack{}
			}
			// fmt.Println(stacks)
			for _, instruction := range instructions {
				for i, charInt := range instruction {
					if charInt >= 65 && charInt <= 90 {
						// fmt.Println(i)
						key := strconv.Itoa((i / 4) + 1)
						if key == "0" {
							key = strconv.Itoa(numStacks)
						}
						stacks[key] = append(stacks[key], string(charInt))
					}
				}
			}
			instructions = []string{}
		}
	}
	for _, instruction := range instructions {
		count, from, to := parseInstruction(instruction)
		// fmt.Println(instruction)
		executeInstruction(stacks, count, from, to)
	}
	out := ""
	for i := 0; i < numStacks; i++ {
		out += stacks[strconv.Itoa(i+1)][0]
	}
	fmt.Println(out)
}
