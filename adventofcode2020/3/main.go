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
	m := make([][]rune, 0)
	for i := range m {
		m[i] = make([]rune, 0)
	}

	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatalln("error opening input file:", err)
	}

	reader := bufio.NewReader(file)
	i := 0
	for {
		text, err := reader.ReadString('\n')
		if err != nil {
			if errors.Is(err, io.EOF) {
				break
			}

			log.Fatalln("error reading from input file:", err)
		}

		text = strings.Replace(text, "\n", "", 1)

		n := make([]rune, 0)
		for _, char := range text {
			n = append(n, char)
		}

		m = append(m, n)
		i++
	}

	treesHit1 := solve(m, 3, 1)
	treesHit2 := solve(m, 1, 1) *
		solve(m, 3, 1) *
		solve(m,5, 1) *
		solve(m,7, 1) *
		solve(m,1, 2)

	fmt.Println("trees hit (part 1):", treesHit1)
	fmt.Println("trees hit (part 2):", treesHit2)
}

func printMap(m [][]rune) {
	for i := range m {
		for j := range m[i] {
			fmt.Printf("%c", m[i][j])
		}
		fmt.Println()
	}
}

func solve(m [][]rune, right int, down int) int {
	treesHit := 0

	j := right
	for i := down; i < len(m); i+=down {
		if m[i][j] == '#' {
			treesHit++
		}

		j = (j + right) % len(m[i])
	}

	return treesHit
}
