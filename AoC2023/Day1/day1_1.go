package day01

import (
	"fmt"
	"log"
	"strconv"
	"strings"
)

func MainPart1(input string) {
	sum := 0
	for _, line := range strings.Split(input, "\n") {
		calibrationValue, err := SumOfLine(line)

		if err != nil {
			log.Fatal(err)
		}
		sum += calibrationValue
	}

	fmt.Printf("The sum of all calibration values is %d\n", sum)
}

func IsDigit(chr byte) bool {
	return chr >= '0' && chr <= '9'
}

func SumOfLine(line string) (int, error) {

	first, last := 0, 0

	for i := 0; i < len(line); i++ {
		ch := line[i]
		if IsDigit(ch) {
			first = int(ch - '0')

			for j := len(line) - 1; j >= i; j-- {
				ch = line[j]
				if IsDigit(ch) {
					last = int(ch - '0')
					break
				}
			}
			break
		}
	}

	convertedDigit, err := strconv.Atoi(fmt.Sprintf("%d%d", first, last))
	if err != nil {
		return 0, fmt.Errorf("unable to convert string to integer: %w", err)
	}

	return convertedDigit, nil
}
