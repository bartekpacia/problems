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
	plateNumbers := make([]int, 0, 100)

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

		numberOfPlates, err := strconv.Atoi(text)
		if err != nil {
			log.Fatalln("error parsing int:", err)
		}

		if numberOfPlates == 0 {
			break
		}

		plateNumbers = append(plateNumbers, numberOfPlates)
	}

	for _, tableCount := range plateNumbers {
		buildingCount, err := solve(tableCount)
		if err != nil {
			fmt.Println("Niepoprawne!")
		} else {
			fmt.Println(buildingCount)
		}

	}
}

func solve(countOfPlates int) (int, error) {
	numberOfBuildings := 1
	for countOfPlates > 0 {
		numOfDigits := numberOfDigits(numberOfBuildings)
		countOfPlates -= numOfDigits

		numberOfBuildings++
	}

	if countOfPlates != 0 {
		return 0, errors.New("tables weren't zeroed out")
	}

	countOfBuildings := numberOfBuildings - 1
	return countOfBuildings, nil
}

func numberOfDigits(num int) (digits int) {
	for num > 0 {
		digits++
		num = num / 10
	}

	return digits
}
