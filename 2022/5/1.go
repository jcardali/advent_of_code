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

func executeCM9000Instruction(stacks Stacks, count int, from string, to string) {
	for i := 0; i < count; i++ {
		crate := stacks[from][0]
		stacks[from] = stacks[from][1:]
		stacks[to] = append(Stack{crate}, stacks[to]...)
	}
}

func executeCM9001Instruction(stacks Stacks, count int, from string, to string) {
	var stack = make(Stack, count)
	copy(stack, stacks[from][:count])
	stacks[from] = stacks[from][count:]
	stacks[to] = append(stack, stacks[to]...)
}

func main() {
	f, _ := os.Open("input.txt")

	defer f.Close()

	scanner := bufio.NewScanner(f)
	var instructions []string
	var numStacks int
	var stacks, stacks2 = Stacks{}, Stacks{}

	for scanner.Scan() {
		row := scanner.Text()
		instructions = append(instructions, row)
		if row == "" {
			numberRow := instructions[len(instructions)-2]
			numStacks, _ = strconv.Atoi(string(numberRow[len(numberRow)-2]))
			for i := 0; i < numStacks; i++ {
				key := strconv.Itoa(i + 1)
				stacks[key], stacks2[key] = Stack{}, Stack{}
			}
			for _, instruction := range instructions {
				for i, charInt := range instruction {
					// Ignore whitespace + brackets
					if charInt >= 65 && charInt <= 90 {
						// Crates are four characters
						key := strconv.Itoa((i / 4) + 1)
						charStr := string(charInt)
						stacks[key], stacks2[key] = append(stacks[key], charStr), append(stacks2[key], charStr)
					}
				}
			}
			instructions = []string{}
		}
	}
	for _, instruction := range instructions {
		count, from, to := parseInstruction(instruction)
		executeCM9000Instruction(stacks, count, from, to)
		executeCM9001Instruction(stacks2, count, from, to)
	}
	out, out2 := "", ""
	for i := 0; i < numStacks; i++ {
		key := strconv.Itoa(i + 1)
		out += stacks[key][0]
		out2 += stacks2[key][0]
	}
	fmt.Println(out)
	fmt.Println(out2)
}
