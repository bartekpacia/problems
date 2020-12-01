package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

// 101
// 192
// 32
// 12493
// 0

func main() {
	// fmt.Printf("%d\n", numberOfDigits(1))
	// fmt.Printf("%d\n", numberOfDigits(10))
	// fmt.Printf("%d\n", numberOfDigits(100))
	// fmt.Printf("%d\n", numberOfDigits(1000))

	var tables []int64
	tables = make([]int64, 0, 100)

	reader := bufio.NewReader(os.Stdin)
	for {
		text, _ := reader.ReadString('\n')

		text = strings.Replace(text, "\n", "", 1)

		num, err := strconv.ParseInt(text, 10, 32)
		if err != nil {
			log.Fatalln("error parsing int:", err)
		}

		if num == 0 {
			break
		}

		tables = append(tables, num)

		buildingCount, err := solve(num)
		if err != nil {
			fmt.Println("Niepoprawne!")
		}

		fmt.Println(buildingCount)

	}
	fmt.Print("Enter text: ")
}

func solve(tableCount int64) (buildingCount int64, err error) {
	fmt.Println("number:", tableCount)

	var i int64 = 1
	for tableCount <= 0 {
		numOfDigits := numberOfDigits(i)
		tableCount = tableCount - numOfDigits

		i++
	}

	return buildingCount, nil
}

func numberOfDigits(num int64) (liczbaCyfr int64) {
	for num > 0 {
		liczbaCyfr++
		num = num / 10
	}

	return liczbaCyfr
}
