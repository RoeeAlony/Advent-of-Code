package main

import (
	"fmt"
	"os"
	"regexp"
	"sort"
	"strconv"
)

type Match struct {
	Type     string
	Position int
	Value    int
}

func main() {
	content, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	text := string(content)

	mulPattern := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)
	dontPattern := regexp.MustCompile(`don't\(\)`)
	doPattern := regexp.MustCompile(`do\(\)`)

	var matches []Match

	// Find mul patterns
	mulMatches := mulPattern.FindAllStringSubmatchIndex(text, -1)
	for _, m := range mulMatches {
		num1, _ := strconv.Atoi(text[m[2]:m[3]])
		num2, _ := strconv.Atoi(text[m[4]:m[5]])
		matches = append(matches, Match{
			Type:     "mul",
			Position: m[0],
			Value:    num1 * num2,
		})
	}

	// Find don't patterns
	dontMatches := dontPattern.FindAllStringIndex(text, -1)
	for _, m := range dontMatches {
		matches = append(matches, Match{
			Type:     "dont",
			Position: m[0],
		})
	}

	// Find do patterns
	doMatches := doPattern.FindAllStringIndex(text, -1)
	for _, m := range doMatches {
		matches = append(matches, Match{
			Type:     "do",
			Position: m[0],
		})
	}

	sort.Slice(matches, func(i, j int) bool {
		return matches[i].Position < matches[j].Position
	})

	enabled := true
	total := 0

	// Process matches with switch
	for _, m := range matches {
		switch m.Type {
		case "do":
			enabled = true
		case "dont":
			enabled = false
		case "mul":
			if enabled {
				total += m.Value
			}
		default:
			continue
		}
	}

	fmt.Printf("\nFinal total: %d\n", total)
}
