package main

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"log"
	"os"
	"strings"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalln("error opening input file:", err)
	}

	passports := make([]passport, 0)

	reader := bufio.NewReader(file)
	currentPassport := make(map[string]string)
	for {
		text, err := reader.ReadString('\n')
		if err != nil && !errors.Is(err, io.EOF) {
			log.Fatalln("error reading from input file:", err)
		}

		isEOF := errors.Is(err, io.EOF)
		if text == "\n" || isEOF {
			var p passport
			p.grab(currentPassport)
			passports = append(passports, p)
			currentPassport = make(map[string]string)
			if isEOF {
				// It was EOF, which appears after the last passport.
				break
			}
			// It was a blank line, which separates passports.
			continue
		}

		text = strings.Replace(text, "\n", "", 1)
		spaceSplitties := strings.Split(text, " ")

		for _, split := range spaceSplitties {
			colonSplitties := strings.Split(split, ":")
			key := colonSplitties[0]
			val := colonSplitties[1]

			currentPassport[key] = val
		}
	}

	valid1 := solvePart1(passports)
	valid2 := solvePart2(passports)
	fmt.Printf("valid passports (part 1): %d\n", valid1)
	fmt.Printf("valid passports (part 2): %d\n", valid2)
}

func solvePart1(passports []passport) (valid int) {
	for _, passport := range passports {
		if passport.isValid1() {
			valid++
		}
	}

	return
}

func solvePart2(passports []passport) (valid int) {
	for _, passport := range passports {
		if passport.isValid2() {
			valid++
		}
	}

	return
}
