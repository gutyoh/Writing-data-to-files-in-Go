package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	// DO NOT DELETE! This creates the 'keanu_quotes.txt' file and opens it in read-write mode
	file, err := os.Create("keanu_quotes.txt")
	if err != nil {
		log.Println(err)
	}
	defer file.Close()

	quotes := []string{"You're breathtaking!",
		"Wake up Samurai! We have a city to burn.",
		"Lose? I don't lose; I win! I'm a lawyer, that's my job, that's what I do!",
	}

	for _, ? := range ? { // iterate over each line of the 'quotes' slice here
		_, err := fmt.Fprintln(?, ?) // // write each line of the 'quotes' slice of strings to 'file' here
		if err != nil {
			log.Println(err)
		}
	}
}
