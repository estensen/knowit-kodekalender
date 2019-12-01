package main

import (
	"encoding/csv"
	"io"
	"fmt"
	"log"
	"os"
	"strings"
	"strconv"
)

func main() {
	dragonSize := 50
	daysWithoutFood := 0
	extra := 0 
	sheepPerDay := []int{}

	file, err := os.Open("sau.txt")
	if err != nil {
		log.Fatal(err)
	}
	r := csv.NewReader(file)

	for {
		record, err := r.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			log.Fatal(err)
		}
		for _, value := range record {
			sheep, err := strconv.Atoi(strings.TrimSpace(value))
			if err != nil {
				log.Fatal(err)
			}
			sheepPerDay = append(sheepPerDay, sheep)
		}
	}

	for i, sheep := range sheepPerDay {
		if daysWithoutFood == 5 {
			fmt.Printf("Survived %d days", i-1)
			break
		}
	
		sheep += extra
		extra = 0

		if dragonSize > sheep {
			dragonSize--
			daysWithoutFood++
		} else {
			extra = sheep - dragonSize
			dragonSize++
			daysWithoutFood = 0
		}
	}
}
