package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	f, _ := os.Open("world.txt")
	defer f.Close()

	scanner := bufio.NewScanner(f)
	count := 0

	for scanner.Scan() {
		line := scanner.Text()
		trimmed := strings.Trim(line, " ")
		count += strings.Count(trimmed, " ")
	}

	fmt.Println(count)
}
