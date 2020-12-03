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
	char string
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
		char := split3[0]
		rest3 := split3[1]

		pass := strings.TrimPrefix(rest3, " ")

		input := rule{min: min, max: max, char: char, pass: pass}
		rules = append(rules, input)
	}

	validRules := 0
	for _, rule := range rules {
		// fmt.Printf("min: %d, max: %d, char: %s, pass: %s\n", input.min, input.max, input.char, input.pass)

		count := 0
		for _, char := range rule.pass {
			if string(char) == rule.char {
				count++
			}
		}

		if count >= rule.min && count <= rule.max {
			validRules++
		}
	}

	fmt.Printf("valid rules: %d\n", validRules)
}
