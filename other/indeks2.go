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
	}
	fmt.Print("Enter text: ")
}

func solve(number int) (int, error) {
	fmt.Println("number:", number)

	return 0, nil
}
