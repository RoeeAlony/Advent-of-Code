package main

import (
	"bytes"
	"fmt"
	"math"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	// setup phase
	lines, _ := os.ReadFile("input.txt")
	numberOfRows := bytes.Count(lines, []byte("\n")) + 1
	fmt.Printf("Number of rows: %d\n", numberOfRows)
	leftList := make([]int, numberOfRows)
	rightList := make([]int, numberOfRows)
	totalDiff := 0

	//populate the lists
	for i, line := range strings.Split(string(lines), "\n") {
		leftNumber, rightNumber := parseNumbersFromString(line)
		leftList[i] = leftNumber
		rightList[i] = rightNumber
	}

	//sort phase
	sort.Ints(leftList)
	sort.Ints(rightList)

	//calc phase
	for i := 0; i < numberOfRows; i++ {
		totalDiff += int(math.Abs(float64(leftList[i] - rightList[i])))
	}

	//answer
	fmt.Printf("Total diff: %d\n", totalDiff)
}

func parseNumbersFromString(line string) (int, int) {
	numbers := strings.Fields(line) // Splits on whitespace
	a, _ := strconv.Atoi(numbers[0])
	b, _ := strconv.Atoi(numbers[1])
	return a, b
}
