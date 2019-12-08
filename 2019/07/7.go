package main

import "fmt"

func main() {
	for y := 2; y <= 27644436; y++ {
		b := y * 7
		rest := b % 27644437
		if rest == 1 {
			fmt.Println(5897 * y % 27644437)
			break
		}
	}
}
