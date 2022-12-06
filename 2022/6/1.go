package main

import (
	"bufio"
	"fmt"
	"os"
)

func parsePacket(packet string, uniqueChars int) {
	for idx, _ := range packet {
		countMap := map[string]bool{}
		for i := 0; i < uniqueChars; i++ {
			key := string(packet[idx+i])
			if !countMap[key] {
				countMap[key] = true
			} else {
				break
			}
		}
		if len(countMap) == uniqueChars {
			fmt.Println(idx + uniqueChars)
			break
		}
	}
}

func main() {
	f, _ := os.Open("input.txt")

	defer f.Close()

	scanner := bufio.NewScanner(f)
	packet := ""

	for scanner.Scan() {
		packet = scanner.Text()
	}
	parsePacket(packet, 4)
	parsePacket(packet, 14)
}
