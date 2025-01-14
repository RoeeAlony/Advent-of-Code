/*
package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
)

func main() {
	// Read file
	content, _ := os.ReadFile("input.txt")

	// Regex pattern for mul(n,n) where n is 1-3 digits
	// (\d{1,3}) captures 1-3 digits
	pattern := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)

	// Find all matches
	matches := pattern.FindAllStringSubmatch(string(content), -1)

	total := 0
	for _, match := range matches {
		// match[0] is the full match
		// match[1] is the first number
		// match[2] is the second number
		num1, _ := strconv.Atoi(match[1])
		num2, _ := strconv.Atoi(match[2])
		total += num1 * num2
	}

	fmt.Printf("Total sum: %d\n", total)
}
*/