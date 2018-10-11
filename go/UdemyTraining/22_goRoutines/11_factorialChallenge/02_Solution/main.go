package main

import (
	"fmt"
)

func main() {
	f := factorial(4)
	total := totalizer(f)
	fmt.Println("Total:", <-total)
}

func factorial(n int) <-chan int {
	factors := make(chan int)
	go func() {
		for i := n; i > 0; i-- {
			factors <- i
		}
		close(factors)
	}()
	return factors
}

func totalizer(f <-chan int) chan int {
	total := make(chan int)
	go func() {
		sum := 1
		for n := range f {
			sum *= n
		}
		total <- sum
		close(total)
	}()
	return total
}

/*
CHALLENGE #1:
-- Use goroutines and channels to calculate the factorial

CHALLENGE #2:
-- Why might you want to use goroutines and channels to calculate factorials?

*/
