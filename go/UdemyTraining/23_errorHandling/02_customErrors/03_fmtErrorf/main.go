package main

import (
	"fmt"
	"log"
)

func main() {
	_, err := sqrt(-10)
	if err != nil {
		log.Fatalln(err)
	}
}

func sqrt(f float64) (float64, error) {
	if f < 0 {
		return 0, fmt.
			Errorf("norgate math again: square root of a negative number : %v",
				f)
	}
	//implementation
	return 42, nil
}
