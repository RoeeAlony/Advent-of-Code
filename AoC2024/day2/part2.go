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
	counter := 0

	for _, line := range bytes.Split(lines, []byte("\n")) {
		report, _ := bytesToInts(line)
		if isAscendingWithRefactor(report) || isDescendingWithRefactor(report) {
			counter++
		}
	}
	fmt.Printf("part 2 answer: %d\n", counter)
}

func isAscendingWithRefactor(report []int) bool {
	for i := 0; i < len(report)-1; i++ {
		if report[i] >= report[i+1] || report[i+1]-report[i] > 3 {
			newReport := newListWithSkip(report, i+1)
			if isAscending(newReport) {
				return true
			}
			newReport2 := newListWithSkip(report, i)
			return isAscending(newReport2)
		}
	}
	return true
}

func isAscending(report []int) bool {
	for i := 0; i < len(report)-1; i++ {
		if report[i] >= report[i+1] || report[i+1]-report[i] > 3 {
			return false
		}
	}
	return true
}

func newListWithSkip(report []int, skip int) []int {
	newReport := make([]int, len(report)-1)
	for j := 0; j < len(report); j++ {
		if j < skip {
			newReport[j] = report[j]
		}
		if j > skip {
			newReport[j-1] = report[j]
		}
	}
	return newReport
}

func isDescending(report []int) bool {
	for i := 0; i < len(report)-1; i++ {
		if report[i] <= report[i+1] || report[i]-report[i+1] > 3 {
			return false
		}
	}
	return true
}

func isDescendingWithRefactor(report []int) bool {
	for i := 0; i < len(report)-1; i++ {
		if report[i] <= report[i+1] || report[i]-report[i+1] > 3 {
			newReport := newListWithSkip(report, i+1)
			if isDescending(newReport) {
				return true
			}
			newReport2 := newListWithSkip(report, i)
			return isDescending(newReport2)
		}
	}
	return true
}

func bytesToInts(data []byte) ([]int, error) {
	// Convert bytes to string and split by whitespace
	strNumbers := strings.Fields(string(data))

	// Create slice to hold the numbers
	numbers := make([]int, len(strNumbers))

	// Convert each string to integer
	for i, str := range strNumbers {
		num, err := strconv.Atoi(str)
		if err != nil {
			return nil, err
		}
		numbers[i] = num
	}

	return numbers, nil
}
