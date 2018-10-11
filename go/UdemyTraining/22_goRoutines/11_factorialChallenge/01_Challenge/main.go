package main

import (
	"fmt"
)

func main() {
	f := factorial(4)
	fmt.Println("Total:", f)
}

func factorial(n int) int {
	total := 1
	for i := n; i > 0; i-- {
		total *= i
	}
	return total
}

/*
CHALLENGE #1:
-- Use goroutines and channels to calculate the factorial

CHALLENGE #2:
-- Why might you want to use goroutines and channels to calculate factorials?

*/
