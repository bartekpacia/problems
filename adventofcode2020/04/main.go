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

type passport struct {
	// Birth Year
	byr *int
	// Issue Year
	iyr *int
	// Expiration Year
	eyr *int
	// Height
	hgt *int
	// Hair Color
	hcl *string
	// Eye Color
	ecl *string
	// Passport ID
	pid *int
	// Country ID
	cid *int
}

func (p *passport) isValid() bool {
	if p.byr == nil ||
		p.iyr == nil ||
		p.eyr == nil ||
		p.hgt == nil ||
		p.hcl == nil ||
		p.ecl == nil ||
		p.pid == nil {
		return false
	}

	return true
}

func main() {
	file, err := os.Open("inputt.txt")
	if err != nil {
		log.Fatalln("error opening input file:", err)
	}

	passports := make([]passport, 0)

	reader := bufio.NewReader(file)
	currentPassport := passport{}
	for {
		text, err := reader.ReadString('\n')
		if err != nil {
			if errors.Is(err, io.EOF) {
				break
			}

			log.Fatalln("error reading from input file:", err)
		}

		if text == "\n" {
			// It was a blank line, which separates passports.
			passports = append(passports, currentPassport)
			currentPassport = passport{}
			continue
		} else {
			text = strings.Replace(text, "\n", "", 1)
		}
	}

	valid := 0
	for _, passport := range passports {
		if passport.isValid() {
			valid++
		}
	}

	fmt.Printf("valid passports (part 1): %d\n", valid)
}
