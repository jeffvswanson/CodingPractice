package main

import "fmt"

func main() {
	list := greatest(1, 2, 5, 8, 99, 10, 20, 45)
	fmt.Println(list)
}

func greatest(sf ...int) int {
	var largest int
	for _, n := range sf {
		if n > largest {
			largest = n
		}
	}
	return largest
}

/*
Write a function with one variadic parameter that finds the greatest
number in a list of numbers.
*/
