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
	currentDir := ""
	var directoryList []string
	directorySizes := map[string]int{}

	for scanner.Scan() {
		command := scanner.Text()
		split := strings.Split(command, " ")
		if string(split[0]) == "$" {
			if split[1] == "cd" {
				currentDir = split[2]
				if currentDir == ".." {
					directoryList = directoryList[:len(directoryList)-1]
				} else {
					directoryList = append(directoryList, currentDir)
				}
				// fmt.Println(directoryList)
			}
		} else if string(split[0]) != "dir" {
			size, _ := strconv.Atoi(split[0])
			for _, directory := range directoryList {
				if currSize, ok := directorySizes[directory]; ok {
					directorySizes[directory] = currSize + size
				} else {
					directorySizes[directory] = size
				}
			}
			fmt.Println(directorySizes)
		}
	}
	totalSize := 0
	for _, size := range directorySizes {
		if size <= 100000 {
			// fmt.Println(name, size)
			totalSize += size
		}
	}
	// 1151021 is low
	fmt.Println(totalSize)
}
