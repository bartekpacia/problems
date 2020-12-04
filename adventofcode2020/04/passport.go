package main

import "strconv"

// Passport represents a single passport read from the input file.
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

func (p *passport) isValid1() bool {
	return p.byr != 0 &&
		p.iyr != 0 &&
		p.eyr != 0 &&
		p.hgt != "" &&
		p.hcl != "" &&
		p.ecl != "" &&
		p.pid != ""
}

func (p *passport) isValid2() bool {
	return p.isValid1() &&
		birthYearValid(p.byr) &&
		issueYearValid(p.iyr) &&
		expirationYearValid(p.eyr) &&
		heightValid(p.hgt) &&
		hairColorValid(p.hcl) &&
		eyeColorValid(p.ecl) &&
		passportIDvalid(p.pid)
}

func birthYearValid(year int) bool {
	return year >= 1920 && year <= 2002
}

func issueYearValid(year int) bool {
	return year >= 2010 && year <= 2020
}

func expirationYearValid(year int) bool {
	return year >= 2020 && year <= 2030
}

func heightValid(height string) bool {
	num, _ := strconv.Atoi(height[:len(height)-2])
	unit := height[len(height)-2:]

	if unit == "in" {
		return num >= 59 && num <= 76
	} else if unit == "cm" {
		return num >= 150 && num <= 193
	}

	return false
}

func hairColorValid(color string) bool {
	if len(color) != 7 {
		return false
	}

	if color[0] != '#' {
		return false
	}

	for _, r := range color[1:7] {
		isDigit := int(r) >= 48 && int(r) <= 57
		isChar := int(r) >= 97 && int(r) <= 122

		if !isDigit && !isChar {
			return false
		}
	}

	return true
}

func eyeColorValid(color string) bool {
	validColors := []string{"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

	for _, validColor := range validColors {
		if validColor == color {
			return true
		}
	}

	return false
}

func passportIDvalid(passportID string) bool {
	if len(passportID) != 9 {
		return false
	}

	_, err := strconv.Atoi(passportID)

	return err == nil
}
