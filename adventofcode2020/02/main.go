package main

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"log"
	"os"
	"strconv"
	"strings"
)

type rule struct {
	min  int
	max  int
	char rune
	pass string
}

func main() {
	rules := make([]rule, 0, 1000)
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalln(err)
	}

	reader := bufio.NewReader(file)
	for {
		text, err := reader.ReadString('\n')
		if err != nil {
			if errors.Is(err, io.EOF) {
				break
			}

			log.Fatalln("error reading from reader:", err)
		}

		text = strings.Replace(text, "\n", "", 1)
		split1 := strings.SplitN(text, "-", 2)
		rest1 := split1[1]
		minStr := split1[0]
		min, _ := strconv.Atoi(minStr)

		split2 := strings.SplitN(rest1, " ", 2)
		rest2 := split2[1]
		maxStr := split2[0]
		max, _ := strconv.Atoi(maxStr)

		split3 := strings.SplitN(rest2, ":", 2)
		char := split3[0][0]
		rest3 := split3[1]

		pass := strings.TrimPrefix(rest3, " ")

		input := rule{min: min, max: max, char: rune(char), pass: pass}
		rules = append(rules, input)
	}

	fmt.Printf("valid rules (part 1): %d\n", solvePart1(rules))
	fmt.Printf("valid rules (part 2): %d\n", solvePart2(rules))
}

func solvePart1(rules []rule) int {
	validRules := 0
	for _, rule := range rules {
		count := 0
		for _, char := range rule.pass {
			if char == rule.char {
				count++
			}
		}

		if count >= rule.min && count <= rule.max {
			validRules++
		}
	}

	return validRules
}

func solvePart2(rules []rule) int {
	validRules := 0

	for _, rule := range rules {
		presentAtMin := false
		i := rule.min - 1
		first := rune(rule.pass[i])
		if first == rule.char {
			presentAtMin = true
		}

		presentAtMax := false
		j := rule.max - 1
		second := rune(rule.pass[j])
		if second == rule.char {
			presentAtMax = true
		}

		if presentAtMin != presentAtMax {
			validRules++
		}
	}

	return validRules
}
