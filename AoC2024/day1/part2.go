package main

import (
	"bytes"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	// setup phase
	lines, _ := os.ReadFile("input.txt")
	numberOfRows := bytes.Count(lines, []byte("\n")) + 1
	leftDict := make(map[int]int)
	rightList := make([]int, numberOfRows)
	total := 0

	//populate the lists
	for i, line := range strings.Split(string(lines), "\n") {
		leftNumber, rightNumber := parseNumbersFromString(line)
		leftDict[leftNumber] = 0
		rightList[i] = rightNumber
	}

	//sort phase
	for _, num := range rightList {
		if value, ok := leftDict[num]; ok {
			leftDict[num] = value + 1
		}
	}

	//calc phase
	for key, value := range leftDict {
		total += key * value
	}

	//answer
	fmt.Printf("Total diff: %d\n", total)
}

func parseNumbersFromString(line string) (int, int) {
	numbers := strings.Fields(line)
	a, _ := strconv.Atoi(numbers[0])
	b, _ := strconv.Atoi(numbers[1])
	return a, b
}
