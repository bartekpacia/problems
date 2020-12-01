package main

import (
	"bufio"
	"errors"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	tables := make([]int, 0, 100)

	file, err := os.Open("test.txt")
	if err != nil {
		log.Fatalln("error opening test.txt:", err)
	}

	reader := bufio.NewReader(file)
	for {
		text, err := reader.ReadString('\n')
		if err != nil {
			log.Fatalln("error reading from reader:", err)
		}

		text = strings.Replace(text, "\n", "", 1)

		num, err := strconv.Atoi(text)
		if err != nil {
			log.Fatalln("error parsing int:", err)
		}

		if num == 0 {
			break
		}

		tables = append(tables, num)
	}

	for _, tableCount := range tables {
		buildingCount, err := solve(tableCount)
		if err != nil {
			fmt.Println("Niepoprawne!")
		} else {
			fmt.Println(buildingCount)
		}

	}
}

func solve(tableCount int) (int, error) {
	buildingNumber := 1
	for tableCount > 0 {
		numOfDigits := numberOfDigits(buildingNumber)
		tableCount -= numOfDigits

		buildingNumber++
	}

	if tableCount != 0 {
		return 0, errors.New("tables weren't zeroed out")
	}

	buildingCount := buildingNumber - 1
	return buildingCount, nil
}

func numberOfDigits(num int) (digits int) {
	for num > 0 {
		digits++
		num = num / 10
	}

	return digits
}
