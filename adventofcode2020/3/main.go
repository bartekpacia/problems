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

	printMap(m)
	treesHit, m := solvePart1(m)
	fmt.Println("trees hit:", treesHit)
	printMap(m)
}

func printMap(m [][]rune) {
	for i := range m {
		for j := range m[i] {
			fmt.Printf("%c", m[i][j])
		}
		fmt.Println()
	}
}

func solvePart1(m [][]rune) (int, [][]rune) {
	treesHit := 0

	j := 3
	for i := 1; i < len(m); i+=1 {
		if m[i][j] == '#' {
			treesHit++
			m[i][j] = 'X'
		} else {
			m[i][j] = 'O'
		}

		j = (j + 3) % len(m[i])


		//for j := 0; j < len(m[i]); j+=3 {
		//	if m[i][j] == '#' {
		//		treesHit++
		//		m[i][j] = 'T'
		//	}
		//}
	}


	return treesHit, m
}
