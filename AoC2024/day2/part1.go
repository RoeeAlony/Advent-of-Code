/*
package main

import (
	"bytes"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func part1() {
	// setup phase
	lines, _ := os.ReadFile("input.txt")
	counter := 0

	for _, line := range bytes.Split(lines, []byte("\n")) {
		report, _ := bytesToInts(line)
		if isAscending(report) || isDescending(report) {
			counter++
		}
	}
	fmt.Printf("part 1 answer: %d\n", counter)
}

func isAscending(report []int) bool {
	for i := 0; i < len(report)-1; i++ {
		// Check each adjacent pair
		if report[i] >= report[i+1] || report[i+1]-report[i] > 3 {
			return false
		}
	}
	return true
}

func isDescending(report []int) bool {
	for i := 0; i < len(report)-1; i++ {
		// Check each adjacent pair
		if report[i] <= report[i+1] || report[i]-report[i+1] > 3 {
			return false
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
*/