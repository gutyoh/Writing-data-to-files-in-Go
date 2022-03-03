package main

import (
	"fmt"
	"log"
	"os"
)

func main() {
	// DO NOT DELETE! This creates the 'galley_grub.txt' file and then opens it in read-write mode
	file, err := os.OpenFile("galley_grub.txt", os.O_APPEND, 0644)
	if err != nil {
		log.Println(err)
	}
	defer file.Close()

	// write "Kelp Shake $2.00" to the 'file' variable below with the fmt.Fprintln() function
	_, err = fmt.Fprintln(?, "?")
	if err != nil {
		log.Println(err)
	}
}
