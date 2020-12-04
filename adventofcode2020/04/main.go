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

func (p *passport) grab(vals map[string]string) {
	var err error
	if vals["byr"] != "0" {
		p.byr, err = strconv.Atoi(vals["byr"])
		if err != nil {
			fmt.Printf("vals[byr] was %#v: %v\n", vals["byr"], err)
		}
	}
	if vals["iyr"] != "0" {
		p.iyr, err = strconv.Atoi(vals["iyr"])
		if err != nil {
			fmt.Printf("vals[iyr] was %#v: %v\n", vals["iyr"], err)
		}
	}
	if vals["eyr"] != "0" {
		p.eyr, err = strconv.Atoi(vals["eyr"])
		if err != nil {
			fmt.Printf("vals[eyr] was %#v: %v\n", vals["eyr"], err)
		}
	}
	if vals["hgt"] != "0" {
		p.hgt = vals["hgt"]
	}
	if vals["hcl"] != "0" {
		p.hcl = vals["hcl"]
	}
	if vals["ecl"] != "0" {
		p.ecl = vals["ecl"]
	}
	if vals["pid"] != "0" {
		p.pid = vals["pid"]
	}
	if vals["cid"] != "0" {
		p.cid, err = strconv.Atoi(vals["cid"])
		if err != nil {
			fmt.Printf("vals[cid] was %#v: %v\n", vals["cid"], err)
		}
	}
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

		// fmt.Println(len(splitties2), splitties2)
	}

	valid := 0
	for _, passport := range passports {
		fmt.Printf("%#v\n", passport)
		if passport.isValid() {
			fmt.Println(passport.pid, "is valid")
			valid++
		} else {
			fmt.Println(passport.pid, "is invalid")
		}
	}

	fmt.Printf("valid passports (part 1): %d\n", valid)
}
