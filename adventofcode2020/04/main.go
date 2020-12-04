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

type passport struct {
	// Birth Year
	byr int
	// Issue Year
	iyr int
	// Expiration Year
	eyr int
	// Height
	hgt string
	// Hair Color
	hcl string
	// Eye Color
	ecl string
	// Passport ID
	pid string
	// Country ID
	cid int
}

// Grab retrieves all properties from vals and assigns them
// to passport pointed to by p.
func (p *passport) grab(vals map[string]string) {
	p.byr, _ = strconv.Atoi(vals["byr"])
	p.iyr, _ = strconv.Atoi(vals["iyr"])
	p.eyr, _ = strconv.Atoi(vals["eyr"])
	p.hgt = vals["hgt"]
	p.hcl = vals["hcl"]
	p.ecl = vals["ecl"]
	p.pid = vals["pid"]
	p.cid, _ = strconv.Atoi(vals["cid"])
}

func (p *passport) isValid() bool {
	return p.byr != 0 &&
		p.iyr != 0 &&
		p.eyr != 0 &&
		p.hgt != "" &&
		p.hcl != "" &&
		p.ecl != "" &&
		p.pid != ""
}

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
			// It was a blank line, which separates passports.
			var p passport
			p.grab(currentPassport)
			passports = append(passports, p)
			currentPassport = make(map[string]string)
			if isEOF {
				break
			}
			continue
		}

		text = strings.Replace(text, "\n", "", 1)
		spaceSplitties := strings.Split(text, " ")

		splitties2 := make([]string, 0)
		for _, split := range spaceSplitties {
			colonSplitties := strings.Split(split, ":")
			key := colonSplitties[0]
			val := colonSplitties[1]
			splitties2 = append(splitties2, val)

			currentPassport[key] = val
		}
	}

	valid := solvePart1(passports)
	fmt.Printf("valid passports (part 1): %d\n", valid)
}

func solvePart1(passports []passport) (valid int) {
	for _, passport := range passports {
		if passport.isValid() {
			valid++
		}
	}

	return
}
